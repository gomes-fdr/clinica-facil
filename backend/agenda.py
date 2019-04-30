from flask import Blueprint, current_app, jsonify, request
from .token import token_required
from backend.models.agenda import Local, Horario
from backend.models.profissional import Profissional
from .serealizer import LocalSchema, HorarioSchema

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
def get_horario_profissional():
    """
    Busca Horarios de um profissional, por intervalo de datas para atendimento
    """
    return jsonify({'message': 'Horario already exists'}), 405

    
