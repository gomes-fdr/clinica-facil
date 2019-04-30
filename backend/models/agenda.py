from . import db

class Local(db.Model):
    """
    Local onde são realizadas as consultas
    """
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100))


class Horario(db.Model):
    """
    Horarios de profissionais em suas salas
    """
    id = db.Column(db.Integer, primary_key=True)
    dt_dia = db.Column(db.Date)
    hora_ini = db.Column(db.String(5))
    hora_fim = db.Column(db.String(5))
    duracao = db.Column(db.Integer)
    livre = db.Column(db.Boolean, default=True)

    local_id = db.Column(db.Integer, db.ForeignKey('local.id'))
    profissional_id = db.Column(db.Integer, db.ForeignKey('profissional.id'))

    profissionais = db.relationship('Profissional', backref='profissional')
    locais = db.relationship('Local', backref='local')


class Consulta(db.Model):
    """
    Consulta de Pacientes em tratamento na clinica
    """
    id = db.Column(db.Integer, primary_key=True)
    dt_marcacao = db.Column(db.Date)
    compareceu = db.Column(db.Boolean, default=False)
    confirmacao_consulta_sms = db.Column(db.Boolean, default=False)

    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.id'))
    profissional_id = db.Column(db.Integer, db.ForeignKey('profissional.id'))
    horario_id = db.Column(db.Integer, db.ForeignKey('horario.id'))
    convenio_id = db.Column(db.Integer, db.ForeignKey('plano_saude_paciente.id'))

    pacientes = db.relationship('Paciente', backref='pacientes')
    profissionais = db.relationship('Profissional', backref='profissionais')
    horarios = db.relationship('Horario', backref='horario')
    convenios = db.relationship('PlanoSaudePaciente', backref='plano_saude_paciente')