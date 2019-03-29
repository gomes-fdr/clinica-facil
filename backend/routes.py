from flask import render_template
from flask import jsonify, request, current_app
import jwt
from datetime import datetime, timedelta
from functools import wraps

from . import bp

#IMPORTANTE, tem que colocar isso header de solicitação
# headers = {'content-type': 'application/json'} 
# fonte: https://stackabuse.com/single-page-apps-with-vue-js-and-flask-jwt-authentication/

# decorator para protger rotas, somente autenticados com token podem ser acessados
def token_required(f):  
    @wraps(f)
    def _verify(*args, **kwargs):
        auth_headers = request.headers.get('Authorization', '').split()

        invalid_msg = {
            'message': 'Invalid token. Registeration and / or authentication required',
            'authenticated': False
        }
        expired_msg = {
            'message': 'Expired token. Reauthentication required.',
            'authenticated': False
        }

        print(auth_headers)
        print(len(auth_headers))
        if len(auth_headers) != 2:
            return jsonify(invalid_msg), 401

        try:
            token = auth_headers[1]
            data = jwt.decode(token, '0123456789')
            # user = User.query.filter_by(email=data['sub']).first()
            user = {'id': '1', 'email': 'recepcao@clinicadarmas.com.br', 'password': '1234'}
            if not user:
                raise RuntimeError('User not found')
            return f(*args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify(expired_msg), 440
        except (jwt.InvalidTokenError, Exception) as e:
            print(e)
            return jsonify(invalid_msg), 401

    return _verify

@bp.route('/api/v1/status', methods=['GET'])
def status():
    return jsonify({'status': 'ok v1'})

@bp.route('/api/v1/paciente/cpf/<cpf>', methods=['GET'])
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


@bp.route('/api/v1/paciente/nome/<nome>', methods=['GET'])
def paciente_nome(nome):
    return jsonify({'total':0, 'status': 'Not found'})
