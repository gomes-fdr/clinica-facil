from flask import Blueprint, current_app, jsonify, request
from sqlalchemy.exc import SQLAlchemyError

from .token import token_required
from .serealizer import PacienteSchema
from .models import Paciente

bp_paciente = Blueprint('paciente', __name__)

@bp_paciente.route('/api/v1/paciente', methods=['POST'])
def paciente_novo():
    pa = PacienteSchema()

    p, error = pa.load(request.json)

    if error:
        return jsonify(error), 401

    try:
        current_app.db.session.add(p)
        current_app.db.session.commit()
    except SQLAlchemyError as e:
        return jsonify({'message': 'User already in database'}), 403

    return pa.jsonify(p), 201


@bp_paciente.route('/api/v1/paciente/cpf/<cpf>', methods=['GET'])
def paciente_cpf(cpf):
    
    paciente = Paciente.query.filter_by(cpf = cpf).first()

    if not paciente:
        return jsonify({'message': 'Paciente Not Found'}), 404

    return PacienteSchema().jsonify(paciente), 200
    

@bp_paciente.route('/api/v1/paciente/nome/<nome>', methods=['GET'])
@token_required
def paciente_nome(nome):
    return jsonify({'total':0, 'status': 'Not found'}), 404
