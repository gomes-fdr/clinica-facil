from flask import Blueprint, current_app, jsonify, request
from sqlalchemy.exc import SQLAlchemyError
from backend.models.profissional import Profissional

from .token import token_required
from .serealizer import PacienteSchema, ProfissionalSchema, PerfilSchema, SituacaoSchema
from backend.models.profissional import Profissional, Perfil, Situacao

from marshmallow import pprint


bp_profissional = Blueprint('profissional', __name__)

@bp_profissional.route('/api/v1/profissional', methods=['POST'])
def profissional():
    """
    Insere um novo profissional no sistema.
    """
    data = request.json
    perfil = Perfil.query.filter_by(id=data['perfil']).first()
    if not perfil:
        return jsonify({'message': 'Not possible find Perfil'}), 404

    situacao = Situacao.query.filter_by(id=data['situacao']).first()
    if not situacao:
        return jsonify({'message': 'Not possible find Situacao'}), 404

    p = Profissional(
        nome=data['nome'],
        email=data['email'],
        dt_nascimento=data['dt_nascimento'],
        cpf=data['cpf'],
        rg=data['rg'],
        faculdade=data['faculdade'],
        no_conselho=data['no_conselho'],
        perfil=perfil,
        situacao=situacao,
        t_celular=data['t_celular'],
        t_fixo=data['t_fixo'],
        cep=data['cep'],
        rua=data['rua'],
        numero=data['numero'],
        complemento=data['complemento'],
        cidade=data['cidade'],
        estado=data['estado'])

    pa = ProfissionalSchema()

    # https://github.com/marshmallow-code/marshmallow-sqlalchemy/issues/200
    # AttributeError: 'DummySession' object has no attribute 'query' 
    
    # p, error = pa.load(request.json)

    # pprint(p)

    # if error:
    #     return jsonify(error), 401

    if not p:
        return jsonify({'message': 'Not possible create Profissional'}), 400

    try:
        current_app.db.session.add(p)
        current_app.db.session.commit()
    except SQLAlchemyError as e:
        return jsonify({'message': 'User already in database'}), 403

    return pa.jsonify(p), 201

@bp_profissional.route('/api/v1/profissional/cpf/<cpf>', methods=['GET'])
def profissional_cpf(cpf):
    """
    Busca um profissional pelo CPF.
    """
    
    profissional = Profissional.query.filter_by(cpf = cpf).first()

    if not profissional:
        return jsonify({'message': 'Profissional Not Found'}), 404

    return ProfissionalSchema().jsonify(profissional), 200


@bp_profissional.route('/api/v1/profissional/perfil', methods=['GET'])
def perfil():
    """
    Retorna a lista de perfis do sistema
    """
    perfil = Perfil.query.all()

    if not perfil:
        return jsonify({'message': 'Perfil Not Found'}), 404

    return PerfilSchema(many=True).jsonify(perfil), 200


@bp_profissional.route('/api/v1/profissional/situacao', methods=['GET'])
def situacao():
    """
    Retorna a lista de perfis do sistema
    """
    situacao = Situacao.query.all()

    if not situacao:
        return jsonify({'message': 'Situacao Not Found'}), 404

    return SituacaoSchema(many=True).jsonify(situacao), 200