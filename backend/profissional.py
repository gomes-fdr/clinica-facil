from flask import Blueprint, current_app, jsonify, request
from backend.models.profissional import Profissional

from .token import token_required
from .serealizer import PacienteSchema, ProfissionalSchema
from backend.models.profissional import Profissional


bp_profissional = Blueprint('profissional', __name__)

@bp_profissional.route('/api/v1/profissional/cpf/<cpf>', methods=['POST'])
@token_required
def profissional_cpf(cpf):
    """
    Insere um novo profissional no sistema.
    """
    pa = ProfissionalSchema()

    p, error = pa.load(request.json)

    if error:
        return jsonify(error), 401

    try:
        print('Insere no banco')
        print(request.json)
        # current_app.db.session.add(p)
        # current_app.db.session.commit()
    except SQLAlchemyError as e:
        return jsonify({'message': 'User already in database'}), 403

    return pa.jsonify(p), 201

@bp_profissional.route('/api/v1/profissional/nome/<nome>', methods=['POST'])
def profissional_nome(nome):
    pass
