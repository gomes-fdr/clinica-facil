from flask import Blueprint, current_app, jsonify, request
from backend.models.profissional import Profissional

bp_profissional = Blueprint('profissional', __name__)

@bp_profissional.route('/api/v1/profissional/cpf/<cpf>', methods=['POST'])
def profissional_cpf(cpf):
    pass

@bp_profissional.route('/api/v1/profissional/nome/<nome>', methods=['POST'])
def profissional_nome(nome):
    pass
