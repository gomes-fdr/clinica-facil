from flask import Blueprint, request, jsonify, current_app
import jwt
from datetime import datetime, timedelta
from .models import User
from .serealizer import UserSchema

bp_token = Blueprint('token', __name__)

@bp_token.route('/api/v1/token', methods=['POST'])
def token():
    user, error = UserSchema().load(request.json)

    if error:
        return jsonify(error), 401

    user = User.query.filter_by(email=user.email).first()

    if user and user.verify_password(request.json['password']):
        token = jwt.encode({
        'sub': user.email,
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(minutes=60)
        }, '0123456789')
        return jsonify({'token': token.decode('UTF-8')}), 200
    
    return jsonify({'message': 'Credenciais Invalidas', 'authenticated': False}), 401


