from flask import Blueprint, current_app, jsonify, request
from sqlalchemy.exc import SQLAlchemyError

from .token import token_required
from backend.models.paciente import Paciente
from backend.models.ps import PlanoSaude, PlanoSaudePaciente
from .serealizer import PlanoSaudeSchema, PlanoSaudePacienteSchema

bp_ps = Blueprint('plano_saude', __name__)

@bp_ps.route('/api/v1/ps', methods=['GET'])
@token_required
def get_ps():
    """
    Busca planos de saúde
    """
    ps = PlanoSaude.query.all()

    if not ps:
        return jsonify({'message': 'Plano de Saúde not found'}), 404

    return PlanoSaudeSchema(many=True).jsonify(ps), 200


@bp_ps.route('/api/v1/ps/<descricao>', methods=['POST'])
@token_required
def post_ps(descricao):
    """
    Insere novo plano de saúde
    """
    ps = PlanoSaude.query.filter_by(descricao = descricao).first()
    
    if not ps:
        try:
            ps = PlanoSaude(descricao = descricao)
            current_app.db.session.add(ps)
            current_app.db.session.commit()
        except SQLAlchemyError as e:
            return jsonify({'message': 'Fail to add Plano de Saúde'}), 400
    else:
        return jsonify({'message': 'Plano de Saúde already in DB'}), 400

    return PlanoSaudeSchema().jsonify(ps), 201


@bp_ps.route('/api/v1/ps-paciente', methods=['POST'])
def post_ps_paciente():
    """
    Insere um plano de saúde para um paciente
    """
    data = request.json

    ps = PlanoSaude.query.filter_by(id=data['ps']['id']).first()
    paciente = Paciente.query.filter_by(id=data['paciente_id']).first()

    ps_paciente = PlanoSaudePaciente.query.filter_by(paciente_id = paciente.id, ps_id = ps.id).first()

    if not ps_paciente:
        ps_paciente = PlanoSaudePaciente(
            no_carteira = data['no_carteira'],
            dt_validade = data['dt_validade'],
            paciente_id = paciente.id,
            ps_id = ps.id
        )
    else:
        return jsonify({'message': 'Paciente already has this PS'}), 400

    try:
        current_app.db.session.add(ps_paciente)
        current_app.db.session.commit()
    except SQLAlchemyError as e:
        return jsonify({'message': 'Fail to add Plano de Saúde for Paciente'}), 400

    return PlanoSaudePacienteSchema().jsonify(ps_paciente), 201


@bp_ps.route('/api/v1/ps-paciente/<paciente_id>', methods=['GET'])
def get_ps_paciente(paciente_id):
    """
    Busca planos de saúde de um paciente
    """
    ps = PlanoSaudePaciente.query.filter_by(paciente_id = paciente_id).all()

    if not ps:
        return jsonify({'message': 'Plano de Saúde not found'}), 404

    return PlanoSaudePacienteSchema(many=True).jsonify(ps), 200


@bp_ps.route('/api/v1/ps-paciente/delete/<id>', methods=['GET'])
def delete_ps_paciente(id):
    """
    Apaga um plano de saude de um paciente
    """
    print('ID: ' + str(id))
    ps = PlanoSaudePaciente.query.filter_by(id = id).delete()

    if not ps:
        return jsonify({'message': 'Plano de Saúde not found'}), 404
    
    current_app.db.session.commit()

    return jsonify({'message': 'Plano de Saúde removed'}), 200
