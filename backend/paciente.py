from flask import Blueprint, current_app, jsonify, request

from .token import token_required

bp_paciente = Blueprint('paciente', __name__)

# @bp_paciente.route('/api/v1/paciente/cpf/<cpf>', methods=['POST'])
# def paciente_cpf(cpf):
#     pass

# @bp_paciente.route('/api/v1/paciente/nome/<nome>', methods=['POST'])
# def paciente_nome(nome):
#     pass


@bp_paciente.route('/api/v1/paciente/cpf/<cpf>', methods=['GET'])
@token_required
def paciente_cpf(cpf):
    if cpf == '60976900025':
        paciente = {
            'total': 1,
            'nome': 'Fabiano da Rosa Gomes',
            'email': 'gomes.fdr@gmail.com',
            'dt_nascimento': '24/05/1974',
            'rg': '8051099541',
            'cpf': '60976900025',
            'filiacao': 'Marion da Rosa Gomes',
            'profissao': 'Desenvolvedor',
            'responsavel': '',
            't_celular': '51995432916',
            't_fixo': '',
            't_responsavel': '',
            'endereco': {
                'cep': '91720430',
                'rua': 'Silvério Souto',
                'numero': '380',
                'complemento': '',
                'cidade': 'Porto Alegre',
                'estado': 'RS',
            },
            'envioSMS': True,
            'adultoInapto': True
        }
        return jsonify(paciente), 200
    else:
        paciente = {
            'total':0,
            'status': 'Not found' 
        }
    return jsonify(paciente), 404


@bp_paciente.route('/api/v1/paciente/nome/<nome>', methods=['GET'])
@token_required
def paciente_nome(nome):
    return jsonify({'total':0, 'status': 'Not found'}), 404
