import os

from datetime import datetime, timedelta

from flask_jwt_extended import create_access_token
from flask import Blueprint, current_app, jsonify, request

from backend.models.profissional import User, Perfil, Profissional, Situacao
from .serealizer import UserSchema

bp_token = Blueprint('token', __name__)

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

       token = create_access_token(
            identity = {
                'email': user.email,
                'nome': profissional.nome,
                'profile': perfil.descricao,
                'profissional_id': profissional.id,
                'situacao': situacao.descricao
            },
            expires_delta = timedelta(minutes=(60*4)))

       return jsonify({'token': token}), 200
    
    return jsonify({'message': 'Invalid Credentials'}), 401
    
