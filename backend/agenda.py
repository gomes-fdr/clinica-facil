from datetime import datetime
from flask import Blueprint, current_app, jsonify, request
from flask_jwt_extended import jwt_required
from backend.models.agenda import Local, Horario, Consulta
from backend.models.profissional import Profissional, Perfil
from .serealizer import LocalSchema, HorarioSchema, ConsultaSchema, PerfilSchema

from sqlalchemy.exc import SQLAlchemyError

bp_agenda = Blueprint('agenda', __name__)

@bp_agenda.route('/api/v1/agenda/sala', methods=['GET'])
@jwt_required
def get_sala():
    """
    Busca sala(s) para atendimento
    """
    local = Local.query.all()
    if not local:
        return jsonify({'message': 'Local not found'}), 404

    return LocalSchema(many=True).jsonify(local), 200


@bp_agenda.route('/api/v1/agenda/sala/<descricao>', methods=['POST'])
@jwt_required
def post_sala(descricao):
    """
    Adiciona sala para atendimento
    """
    local = Local.query.filter_by(descricao = descricao).first()

    if not local:
        try:
            local = Local(descricao = descricao)
            current_app.db.session.add(local)
            current_app.db.session.commit()
        except SQLAlchemyError as e:
            return jsonify({'message': 'Fail to add Local'}), 400

    else:
        return jsonify({'message': 'Local already in DB'}), 400

    return LocalSchema().jsonify(local), 201


@bp_agenda.route('/api/v1/agenda/horario', methods=['POST'])
@jwt_required
def post_horario():
    """
    Adicona um Horário para atendimento
    """
    data = request.json
    if not data:
        return jsonify({'message': 'Data is empty'}), 400

    """
    {
        'date': '2019-05-03T11:18:38.054Z',
        'startTime': '11:00',
        'endTime': '11:45',
        'livre': True,
        'local': 1,
        'name': 'Bianca Ferraz',
        'profissional_id': 264,
        'duracao': 45
    }
    """

    local = Local.query.filter_by(id = data['local_id']).first()
    profissional = Profissional.query.filter_by(id = data['profissional_id']).first()

    if not local or not profissional:
        return jsonify({'message': 'Fail to add Horario'}), 400

    horario = Horario.query.filter_by(
        dt_dia = data['date'],
        hora_ini = data['startTime'],
        hora_fim = data['endTime'],
        duracao = data['duracao'],
        livre = data['livre'],
        local_id = local.id,
        profissional_id = profissional.id
    ).first()

    if not horario:
        horario = Horario(
            dt_dia = data['date'],
            hora_ini = data['startTime'],
            hora_fim = data['endTime'],
            duracao = data['duracao'],
            livre = data['livre'],
            local_id = local.id,
            profissional_id = profissional.id
        )
    else:
        return jsonify({'message': 'Horario already exists'}), 409

    try:
        current_app.db.session.add(horario)
        current_app.db.session.commit()
    except SQLAlchemyError as e:
        print(e)
        return jsonify({'message': 'Fail to add Horaio'}), 400

    return HorarioSchema().jsonify(horario), 201


@bp_agenda.route('/api/v1/agenda/horario/profissional', methods=['GET'])
@jwt_required
def get_horario_profissional():
    """
    Busca Horarios de um profissional, por intervalo de datas para atendimento
    Retorna:
    {
    "dt_dia": "2019-05-04T13:12:21.759000",
    "hora_fim": "11:45",
    "local_id": 1,
    "livre": true,
    "id": 31,
    "duracao": 45,
    "hora_ini": "11:00",
    "profissional_id": 264
    }
    """
    selecao = request.args['selecao']
    dt_inicio = datetime.strptime(request.args['dt_inicio'], '%d/%m/%Y')
    dt_fim = datetime.strptime(request.args['dt_fim'], '%d/%m/%Y')
    livre = request.args['livre'] == 'true'

    profissional_id = None

    if selecao == 'profissional':
        profissional_id = request.args['profissional_id']
        if not profissional_id:
            return jsonify({'message': 'profissional_id is empty'}), 409

        if profissional_id == '*':
            horarios = Horario.query.filter(Horario.dt_dia >= dt_inicio, Horario.dt_dia <= dt_fim, Horario.livre == livre).all()
        else:
            horarios = Horario.query.filter(Horario.dt_dia >= dt_inicio,
                                        Horario.dt_dia <= dt_fim,
                                        Horario.livre == livre,
                                        Horario.profissional_id == profissional_id).all()
    elif selecao == 'especialidade':
        especialidade = request.args['especialdade_id']
        if not especialidade:
            return jsonify({'message': 'especialidade is empty'}), 409
        else:
            perfil = Perfil.query.filter_by(id = especialidade).first()
            profissionais = Profissional.query.filter_by(perfil_id = perfil.id).all()
            horarios = Horario.query.filter(Horario.dt_dia >= dt_inicio,
                                        Horario.dt_dia <= dt_fim,
                                        Horario.livre == livre,
                                        Horario.profissional_id.in_(( p.id for p in profissionais ))).all()
    else:
        return jsonify({'message': 'Invalid parameters'}), 409


    if not horarios:
        return jsonify({'message': 'Horario(s) not found'}), 404

    return HorarioSchema(many=True).jsonify(horarios), 200


@bp_agenda.route('/api/v1/agenda/consulta', methods=['POST'])
@jwt_required
def post_consulta():
    """
    Adiciona uma consulta
    {
        'dataMarcacao': '2019-05-03T00:20:03.364Z',
        'confirmacao_consulta_sms': False,
        'compareceu': False,
        'paciente': {
            'id': 422876,
            'nome': 'Bianca D ´Armas Ferraz'
        },
        'quem_marcou_id': 266,
        'horario_id': 34,
        'convenio': {
            'id': 32,
            'descricao': 'Particular'}
    }
    """

    data = request.json
    print(data)
    
    if not data:
        return jsonify({'message': 'Fail to add Consulta'}), 404

    consulta = Consulta.query.filter_by(
        dt_marcacao = data['dataMarcacao'],
        compareceu = data['compareceu'],
        confirmacao_consulta_sms = data['confirmacao_consulta_sms'],
        paciente_id = data['paciente']['id'],
        profissional_id = data['quem_marcou_id'],
        horario_id = data['horario_id'],
        convenio_id = data['convenio']['id']
    ).first()

    if not consulta:
        consulta = Consulta(
            dt_marcacao = data['dataMarcacao'],
            compareceu = data['compareceu'],
            confirmacao_consulta_sms = data['confirmacao_consulta_sms'],
            paciente_id = data['paciente']['id'],
            profissional_id = data['quem_marcou_id'],
            horario_id = data['horario_id'],
            convenio_id = data['convenio']['id']
        )
    else:
        return jsonify({'message': 'Consulta already exists'}), 409

    horario = Horario.query.filter_by(id = data['horario_id']).first()
    horario.livre = False

    try:
        current_app.db.session.add(consulta)
        current_app.db.session.commit()
    except SQLAlchemyError as e:
        print(e)
        return jsonify({'message': 'Fail to add consulta'}), 400

    return ConsultaSchema().jsonify(consulta), 201


@bp_agenda.route('/api/v1/agenda/especialidades', methods=['GET'])
@jwt_required
def get_especialidades():
    """
    Busca especialidades disponiveis para atendimento
    """

    especialidades = Perfil.query.filter_by(is_especialista = True).all()

    if not especialidades:
        return jsonify({'message': 'Especialidades not found'}), 404

    return PerfilSchema(many=True).jsonify(especialidades), 200



@bp_agenda.route('/api/v1/agenda/consulta', methods=['GET'])
@jwt_required
def get_consulta_profissional():
    """
    Busca Consultas de um profissional, por intervalo de datas para atendimento
    Retorna:
    {
        id:	6
        profissionais:	264
        dt_marcacao:	2019-05-03T01:10:53.901000
        horario:	32
        compareceu:	false
        confirmacao_consulta_sms:	false
        plano_saude_paciente: 32
        pacientes: 422876
    }
    
    """

    selecao = request.args['selecao']
    dt_ini = datetime.strptime(request.args['dt_ini'], '%d/%m/%Y')
    dt_fim = datetime.strptime(request.args['dt_fim'], '%d/%m/%Y')

    if selecao == 'especialidade':
        especialidade_id = request.args['especialidade_id']
        if not especialidade_id:
            return jsonify({'message': 'Especialidade is empty'}), 409
        else:
            perfil = Perfil.query.filter_by(id = especialidade_id).first()
            profissionais = Profissional.query.filter_by(perfil_id = perfil.id).all()
            horarios = Horario.query.filter(
                Horario.dt_dia >= dt_ini,
                Horario.dt_dia <= dt_fim,
                Horario.livre == False,
                Horario.profissional_id.in_(( p.id for p in profissionais ))
            ).all()
            consultas = Consulta.query.filter(
                Consulta.horario_id.in_(( h.id for h in horarios ))
            ).all()
    elif selecao == 't_profissional':
        horarios = Horario.query.filter(
            Horario.dt_dia >= dt_ini,
            Horario.dt_dia <= dt_fim,
            Horario.livre == False,
        ).all()
        consultas = Consulta.query.filter(
            Consulta.horario_id.in_(( h.id for h in horarios ))
        ).all()
    elif selecao == 'profissional':
        profissional_id = request.args['profissional_id']
        horarios = Horario.query.filter(
            Horario.dt_dia >= dt_ini,
            Horario.dt_dia <= dt_fim,
            Horario.livre == False,
            Horario.profissional_id == profissional_id
        ).all()
        consultas = Consulta.query.filter(
            Consulta.horario_id.in_(( h.id for h in horarios ))
        ).all()

    if not consultas:
        return jsonify({'message': 'Consulta(s) not found'}), 404
    
    return ConsultaSchema(many=True).jsonify(consultas), 200


@bp_agenda.route('/api/v1/agenda/consulta/update', methods=['POST'])
@jwt_required
def update_consulta_profissional():
    """
    Atualiza uma consulta
    """
    data = request.json
    if not data:
        return jsonify({'message': 'Fail to update Consulta'}), 404

    print(data)

    if data['acao'] == 'faltou':
        print('Atualiza campos de falta e grava quem disse que faltou')
    
    elif data['acao'] == 'cancelou':
        # TODO: Qual especialidade, se psquiatra configura encaixe
        print('Atualiza campos de cancelamento e grava quem disse que cancelou')

    elif data['acao'] == 'chegou':
        # TODO: Atualiza campo informando que paciente e chegou e quem disse que chegou
        print('Atualiza campos de acolimento')

    elif data['acao'] == 'atendimento':
        # TODO: Atualiza campo informando que paciente está em atendimento
        print('Atualiza campos de atendimento')
    else:
        return jsonify({'message': 'Fail to update Consulta, no action'}), 404

    return jsonify({'message': 'OK'})