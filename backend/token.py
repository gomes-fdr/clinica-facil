import os

from datetime import datetime, timedelta
from functools import wraps

import jwt
from flask import Blueprint, current_app, jsonify, request

from backend.models.profissional import User, Perfil, Profissional, Situacao
from .serealizer import UserSchema

bp_token = Blueprint('token', __name__)

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

        if len(auth_headers) != 2:
            return jsonify(invalid_msg), 401

        try:
            token = auth_headers[1]
            data = jwt.decode(token, os.environ['SALT_TOKEN'])
            user = User.query.filter_by(email=data['sub']).first()
            if not user:
                raise RuntimeError('User not found')
            return f(*args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify(expired_msg), 440
        except (jwt.InvalidTokenError, Exception) as e:
            return jsonify(invalid_msg), 401

    return _verify


#IMPORTANTE, tem que colocar isso header de solicitação
# headers = {'content-type': 'application/json'} 
# fonte: https://stackabuse.com/single-page-apps-with-vue-js-and-flask-jwt-authentication/
@bp_token.route('/api/v1/token', methods=['POST'])
def token():
    """
    Entrega um token valido por 1 hora para o usuário navegar no sistema.
    """
    user, error = UserSchema().load(request.json)

    if error:
        return jsonify(error), 401

    try:
        user = User.query.filter_by(email=user.email).first()
    except:
        return jsonify({'message': 'User not found'}), 401

    try:
        profissional = Profissional.query.filter_by(email=user.email).first()
    except:
        return jsonify({'message': 'Profissional not found'}), 401

    try:    
        perfil = Perfil.query.filter_by(id=profissional.perfil_id).first()
    except:
        return jsonify({'message': 'Perfil not found'}), 401

    try:
        situacao = Situacao.query.filter_by(id=profissional.situacao_id).first()
    except:
        return jsonify({'message': 'Situacao not found'}), 401

    if user and \
       perfil and \
       profissional and \
       situacao.descricao == 'Ativo' and \
       user.verify_password(request.json['password']):

        token = jwt.encode({
        'sub': user.email,
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(minutes=(60*4)),
        'nome': profissional.nome,
        'profile': perfil.descricao,
        'situacao': situacao.descricao
        }, os.environ['SALT_TOKEN'])
        return jsonify({'token': token.decode('UTF-8')}), 200
    
    return jsonify({'message': 'Invalid Credentials'}), 401
    
