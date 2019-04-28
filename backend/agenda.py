from flask import Blueprint, current_app, jsonify, request
from .token import token_required
from backend.models.agenda import Local
from .serealizer import LocalSchema

bp_agenda = Blueprint('agenda', __name__)

@bp_agenda.route('/api/v1/agenda/sala', methods=['GET'])
@token_required
def get_sala():
    """
    Busca sala(s) para atendimento
    """
    local = Local.query.all()
    if not local:
        return jsonify({'message': 'Local not found'}), 404

    return LocalSchema(many=True).jsonify(local), 200


@bp_agenda.route('/api/v1/agenda/sala/<descricao>', methods=['POST'])
@token_required
def post_sala(descricao):
    """
    Busca sala para atendimento
    """
    local = Local.query.filter_by(descricao = descricao).first()

    if not local:
        try:
            local = Local(descricao = descricao)
            current_app.db.session.add(local)
            current_app.db.session.commit()
        except SQLAlchemyError as e:
            return jsonify({'message': 'Fail to add Local'}), 400

    else:
        return jsonify({'message': 'Local already in DB'}), 400

    return LocalSchema().jsonify(local), 201