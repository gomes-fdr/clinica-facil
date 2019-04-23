from flask import Blueprint, current_app, jsonify, request
from sqlalchemy.exc import SQLAlchemyError

from .token import token_required
from backend.models.ps import PlanoSaude
from .serealizer import PlanoSaudeSchema

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

