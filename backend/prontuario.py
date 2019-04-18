from flask import Blueprint, current_app, jsonify, request
from sqlalchemy.exc import SQLAlchemyError

from .token import token_required
from .serealizer import ProntuarioLegadoSchema
from backend.models.prontuario import ProntuarioLegado

bp_prontuario = Blueprint('prontuario', __name__)

# TODO: Revisar sistema de tokens

@bp_prontuario.route('/api/v1/prontuario-legado/paciente/<paciente_id>', methods=['GET'])
def prontuario_leg_paciente(paciente_id):
    """
    Busca prontuario legado, por ID de paciente
    """
    prontuario = ProntuarioLegado.query.filter_by(paciente_id = paciente_id).first()

    if not prontuario:
        return jsonify({'message': 'Prontuario Not Found'}), 404

    return ProntuarioLegadoSchema().jsonify(prontuario), 200