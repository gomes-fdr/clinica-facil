from flask import Blueprint, current_app, jsonify, request
from sqlalchemy.exc import SQLAlchemyError

from flask_jwt_extended import jwt_required
from .serealizer import PacienteSchema
from backend.models.paciente import Paciente

bp_paciente = Blueprint('paciente', __name__)

@bp_paciente.route('/api/v1/paciente', methods=['POST'])
@jwt_required
def paciente_novo():
    """
    Insere um novo paciente no sistema.
    """
    pa = PacienteSchema()

    p, error = pa.load(request.json)

    if error:
        return jsonify(error), 400

    try:
        current_app.db.session.add(p)
        current_app.db.session.commit()
    except SQLAlchemyError as e:
        return jsonify({'message': 'User already in database'}), 403

    return pa.jsonify(p), 201


@bp_paciente.route('/api/v1/paciente/<cpf>', methods=['POST'])
@jwt_required
def paciente_atualizar(cpf):
    """
    Atualiza um paciente no sistema.
    """
    data = request.json
    if not cpf or not data:
        return jsonify({'message': 'Params are empty'}), 400

    paciente = Paciente.query.filter_by(cpf = cpf).first()

    if not paciente:
        return jsonify({'message': 'There are not the PACIENTE'}), 400

    paciente.nome = data['nome']
    paciente.email = data['email']
    paciente.dt_nascimento = data['dt_nascimento']
    paciente.rg = data['rg']
    paciente.filiacao = data['filiacao']
    paciente.profissao = data['profissao']
    paciente.responsavel = data['responsavel']
    paciente.t_celular = data['t_celular']
    paciente.t_fixo = data['t_fixo']
    paciente.t_responsavel = data['t_responsavel']
    paciente.cep = data['cep']
    paciente.rua = data['rua']
    paciente.numero = data['numero']
    paciente.complemento = data['complemento']
    paciente.cidade = data['cidade']
    paciente.estado = data['estado']
    paciente.envioSMS = data['envioSMS']
    paciente.adultoInapto = data['adultoInapto']
    paciente.observacoes = data['observacoes']
    
    try:
        current_app.db.session.commit()
    except SQLAlchemyError as e:
        return jsonify({'message': 'Fail to update PACIENTE'}), 400
     
    return PacienteSchema().jsonify(paciente), 200


@bp_paciente.route('/api/v1/paciente/cpf/<cpf>', methods=['GET'])
@jwt_required
def paciente_cpf(cpf):
    """
    Busca um paciente pelo CPF.
    """
    
    paciente = Paciente.query.filter_by(cpf = cpf).first()

    if not paciente:
        return jsonify({'message': 'Paciente Not Found'}), 404

    return PacienteSchema().jsonify(paciente), 200
    

@bp_paciente.route('/api/v1/paciente/nome/<nome>', methods=['GET'])
@jwt_required
def paciente_nome(nome):
    """
    Busca um paciente pelo nome ou parte dele.
    """
    # pacientes = Paiente.query.filter(Paciente.nome.ilike('%' +nome+ '%')).all()
    pacientes = current_app.db.session.query(Paciente.nome, Paciente.cpf).filter(Paciente.nome.ilike('%' +nome+ '%')).all()

    if not pacientes:
        return jsonify({'message': 'Paciente Not Found'}), 404

    return PacienteSchema(many=True).jsonify(pacientes), 200


@bp_paciente.route('/api/v1/paciente/nome-completo/<nome>', methods=['GET'])
@jwt_required
def paciente_nome_completo(nome):
    """
    Busca um paciente pelo nome ou parte dele.
    Util apenas para uso com nomes vindo da lista de nomes.
    """

    # pacientes = Paiente.query.filter(Paciente.nome.ilike('%' +nome+ '%')).all()
    paciente = Paciente.query.filter_by(nome = nome).first()

    if not paciente:
        return jsonify({'message': 'Paciente Not Found'}), 404

    return PacienteSchema().jsonify(paciente), 200

