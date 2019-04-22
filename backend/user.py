from flask import Blueprint, current_app, jsonify, request

from .serealizer import UserSchema
from .token import token_required

bp_user = Blueprint('user', __name__)

@bp_user.route('/api/v1/create-user', methods=['POST'])
@token_required
def register():
    """
    Adiciona um usuário no sistema.
    """
    us = UserSchema()

    user, error = us.load(request.json)

    if error:
        return jsonify(error), 401

    user.gen_hash()

    current_app.db.session.add(user)
    current_app.db.session.commit()

    return us.jsonify(user), 201
