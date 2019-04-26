from flask import Blueprint, current_app, jsonify, request

bp_agenda = Blueprint('agenda', __name__)

@bp_agenda.route('/api/v1/agenda/sala', methods=['GET'])
def get_sala():
    """
    Busca sala para atendimento
    """
    return jsonify({'message': 'ok'}), 200