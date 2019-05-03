from datetime import datetime
from flask import Blueprint, current_app, jsonify, request
from .token import token_required
from backend.models.agenda import Local, Horario, Consulta
from backend.models.profissional import Profissional
from .serealizer import LocalSchema, HorarioSchema, ConsultaSchema

from sqlalchemy.exc import SQLAlchemyError

bp_agenda = Blueprint('agenda', __name__)

@bp_agenda.route('/api/v1/agenda/sala', methods=['GET'])
@token_required
def get_sala():
    """
    Busca sala(s) para atendimento
    """
    local = Local.query.all()
    if not local:
        return jsonify({'message': 'Local not found'}), 404

    return LocalSchema(many=True).jsonify(local), 200


@bp_agenda.route('/api/v1/agenda/sala/<descricao>', methods=['POST'])
@token_required
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
@token_required
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
@token_required
def get_horario_profissional():
    """
    Busca Horarios de um profissional, por intervalo de datas para atendimento
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
    dt_inicio = datetime.strptime(request.args['dt_inicio'], '%d/%m/%Y')
    dt_fim = datetime.strptime(request.args['dt_fim'], '%d/%m/%Y')
    livre = request.args['livre'] == 'true'

    horario = Horario.query.filter(Horario.dt_dia >= dt_inicio, Horario.dt_dia <= dt_fim, Horario.livre == livre).all()

    if not horario:
        return jsonify({'message': 'Horario not found'}), 404

    return HorarioSchema(many=True).jsonify(horario), 200


@bp_agenda.route('/api/v1/agenda/consulta', methods=['POST'])
@token_required
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
    TODO: Atualizar o horario para ocupado.

    """

    data = request.json
    print(data)
    
    if not data:
        return jsonify({'message': 'Fail do add Consulta'}), 404

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


