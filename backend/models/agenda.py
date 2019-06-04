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
    is_encaixe = db.Column(db.Boolean, default=False)

    local_id = db.Column(db.Integer, db.ForeignKey('local.id'))
    profissional_id = db.Column(db.Integer, db.ForeignKey('profissional.id'))

    profissional = db.relationship('Profissional', backref='profissional')
    local = db.relationship('Local', backref='local')


class Consulta(db.Model):
    """
    Consulta de Pacientes em tratamento na clinica
    """
    id = db.Column(db.Integer, primary_key=True)
    dt_marcacao = db.Column(db.Date)

    # Avisa que paciente chegou
    b_chegou = db.Column(db.Boolean, default=False)
    p_id_chegou = db.Column(db.Integer, db.ForeignKey('profissional.id'), nullable=True)
    p_chegou = db.relationship('Profissional', foreign_keys=p_id_chegou)

    # Atesta que paciente compareceu a consulta
    b_compareceu = db.Column(db.Boolean, default=False)
    p_id_compareceu = db.Column(db.Integer, db.ForeignKey('profissional.id'), nullable=True)
    p_compareceu = db.relationship('Profissional', foreign_keys=p_id_compareceu)

    # Avisa que paciente não compareceu a consulta
    b_cancelou = db.Column(db.Boolean, default=False)
    p_id_cancelou = db.Column(db.Integer, db.ForeignKey('profissional.id'), nullable=True)
    p_cancelou = db.relationship('Profissional', foreign_keys=p_id_cancelou)
    dt_cancelamento = db.Column(db.Date, nullable=True)

    # Sinaliza que o horário está disponível para uso
    b_encaixe = db.Column(db.Boolean, default=False)
    p_id_encaixe = db.Column(db.Integer, db.ForeignKey('profissional.id'), nullable=True)
    p_encaixe = db.relationship('Profissional', foreign_keys=p_id_encaixe)

    # guarda a confirmação do paciente recebido via SMS
    confirmacao_consulta_sms = db.Column(db.Boolean, default=False)

    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.id'))

    # quem marcou a consulta
    p_id_quem_marcou = db.Column(db.Integer, db.ForeignKey('profissional.id'), nullable=False)
    p_quem_marcou = db.relationship('Profissional', foreign_keys=p_id_quem_marcou)

    horario_id = db.Column(db.Integer, db.ForeignKey('horario.id'))
    convenio_id = db.Column(db.Integer, db.ForeignKey('plano_saude_paciente.id'))

    paciente = db.relationship('Paciente', backref='pacientes')
    horario = db.relationship('Horario', backref='horario')
    plano_saude_paciente = db.relationship('PlanoSaudePaciente', backref='plano_saude_paciente')