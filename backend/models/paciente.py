from . import db


class Paciente(db.Model):
    """
    Pacientes tratados na clinica
    """
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100))
    dt_nascimento = db.Column(db.DateTime, nullable=False)
    cpf = db.Column(db.String(11), index=True, unique=True, nullable=False)
    rg = db.Column(db.String(10))
    filiacao = db.Column(db.String(100), nullable=False)
    profissao = db.Column(db.String(100))
    responsavel = db.Column(db.String(100))
    t_celular = db.Column(db.String(20))
    t_fixo = db.Column(db.String(20))
    t_responsavel = db.Column(db.String(20))
    cep = db.Column(db.String(15))
    rua = db.Column(db.String(100), nullable=False)
    numero = db.Column(db.String(10), nullable=False)
    complemento = db.Column(db.String(100))
    cidade = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.String(100), nullable=False)
    envioSMS = db.Column(db.Boolean, default=False)
    adultoInapto = db.Column(db.Boolean, default=False)

