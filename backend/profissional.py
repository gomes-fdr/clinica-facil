from flask import Blueprint, current_app, jsonify, request
from sqlalchemy.exc import SQLAlchemyError
from backend.models.profissional import Profissional

from flask_jwt_extended import jwt_required
from .serealizer import PacienteSchema, ProfissionalSchema, PerfilSchema, SituacaoSchema
from backend.models.profissional import Profissional, Perfil, Situacao, User

from marshmallow import pprint

bp_profissional = Blueprint('profissional', __name__)


@bp_profissional.route('/api/v1/profissional', methods=['POST'])
@jwt_required
def profissional():
    """
    Insere um novo profissional no sistema.
    """
    data = request.json
    if not data:
        return jsonify({'message': 'There are not params'}), 400

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
    except:
        return jsonify({'message': 'User already in database'}), 403

    # Cria novo profissional com senha padrão '1234'
    p.create_user(p)
    return pa.jsonify(p), 201

@bp_profissional.route('/api/v1/profissional/cpf/<cpf>', methods=['GET'])
@jwt_required
def profissional_cpf(cpf):
    """
    Busca um profissional pelo CPF.
    """
    if not cpf:
        return jsonify({'message': 'Bad params'}), 404
    
    profissional = Profissional.query.filter_by(cpf = cpf).first()

    if not profissional:
        return jsonify({'message': 'Profissional Not Found'}), 404

    return ProfissionalSchema().jsonify(profissional), 200


@bp_profissional.route('/api/v1/profissional/perfil', methods=['GET'])
@jwt_required
def perfil():
    """
    Retorna a lista de perfis do sistema
    """
    perfil = Perfil.query.all()

    if not perfil:
        return jsonify({'message': 'Perfil Not Found'}), 404

    return PerfilSchema(many=True).jsonify(perfil), 200


@bp_profissional.route('/api/v1/profissional/situacao', methods=['GET'])
@jwt_required
def situacao():
    """
    Retorna a lista de situacoes do sistema
    """
    situacao = Situacao.query.all()

    if not situacao:
        return jsonify({'message': 'Situacao Not Found'}), 404

    return SituacaoSchema(many=True).jsonify(situacao), 200


@bp_profissional.route('/api/v1/profissional/nome/<nome>', methods=['GET'])
@jwt_required
def profissional_nome(nome):
    """
    Busca um profissional pelo nome ou parte dele.
    """
    if not nome:
        return jsonify({'message': 'Bad param'}), 400

    # pacientes = Paiente.query.filter(Paciente.nome.ilike('%' +nome+ '%')).all()
    profissionais = current_app.db.session.query(Profissional.id, Profissional.nome, Profissional.cpf).filter(Profissional.nome.ilike('%' +nome+ '%')).all()
    if not profissionais:
        return jsonify({'message': 'Profissional Not Found'}), 404

    return ProfissionalSchema(many=True).jsonify(profissionais), 200


@bp_profissional.route('/api/v1/profissional/<nome>', methods=['POST'])
@jwt_required
def profissional_atualizar(nome):
    """
    Atualiza um profissional no sistema.
    """
    data = request.json
    profissional = Profissional.query.filter_by(nome = nome).first()

    if not profissional:
        return jsonify({'message': 'Profissional Not Found'}), 404

    profissional.nome = data['nome']
    profissional.email = data['email']
    profissional.dt_nascimento = data['dt_nascimento']
    profissional.cpf = data['cpf']
    profissional.rg = data['rg']
    profissional.faculdade = data['faculdade']
    profissional.no_conselho = data['no_conselho']
    profissional.perfil_id = data['perfis']
    profissional.situacao_id = data['situacoes']
    profissional.t_celular = data['t_celular']
    profissional.t_fixo = data['t_fixo']
    profissional.cep = data['cep']
    profissional.rua = data['rua']
    profissional.numero = data['numero']
    profissional.complemento = data['complemento']
    profissional.cidade = data['cidade']
    profissional.estado = data['estado']
    
    try:
        current_app.db.session.commit()
    except SQLAlchemyError as e:
        return jsonify({'message': 'Fail to update PROFISSIONAL'}), 400
     
    return ProfissionalSchema().jsonify(profissional), 200


@bp_profissional.route('/api/v1/profissional/nome-completo/<nome>', methods=['GET'])
@jwt_required
def profissional_nome_completo(nome):
    """
    Busca um profissional pelo nome ou parte dele.
    Util apenas para uso com nomes vindo da lista de nomes.
    """

    # pacientes = Paiente.query.filter(Paciente.nome.ilike('%' +nome+ '%')).all()
    profissional = Profissional.query.filter_by(nome = nome).first()

    if not profissional:
        return jsonify({'message': 'Profissional Not Found'}), 404

    return ProfissionalSchema().jsonify(profissional), 200


@bp_profissional.route('/api/v1/profissional/reset-senha', methods=['POST'])
@jwt_required
def profissional_reset_senha():
    """
    Inicializa Profissional com senha
    """
    data = request.json
    if not data:
        return jsonify({'status': 'Password update fail, no fields'}), 400

    if not data['id_profissional'] or not data['password']:
        return jsonify({'status': 'Password update fail, fields empty'}), 400

    profissional = Profissional.query.filter_by(id = data['id_profissional']).first()

    if not profissional:
        return jsonify({'message': 'Profissional Not Found'}), 404

    usuario = User.query.filter_by(email=profissional.email).first()
    if usuario:
        profissional.update_password(profissional, data['password'])
    else:
        profissional.create_user(profissional)

    return jsonify({'status': 'Password updated'}), 200
