from flask import render_template
from flask import jsonify, request
from app.core import bp

@bp.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@bp.route('/paciente', methods=['GET', 'POST'])
def paciente():
    return render_template('paciente.html')

@bp.route('/api/v1/paciente/<cpf>', methods=['GET'])
def paciente_api(cpf):
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
            'situacao': 'Não encontrado' 
        }
    return jsonify(paciente), 404