from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

db = SQLAlchemy()

def configure(app):
    db.init_app(app)
    app.db = db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.password = generate_password_hash(password)

    def gen_hash(self):
        self.password = generate_password_hash(self.password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)


class Paciente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    dt_nascimento = db.Column(db.DateTime)
    cpf = db.Column(db.String(11), index=True, unique=True)
    rg = db.Column(db.String(10))
    filiacao = db.Column(db.String(100))
    profissao = db.Column(db.String(100))
    responsavel = db.Column(db.String(100))
    t_celular = db.Column(db.String(20))
    t_fixo = db.Column(db.String(20))
    t_responsavel = db.Column(db.String(20))
    cep = db.Column(db.String(15))
    rua = db.Column(db.String(100))
    numero = db.Column(db.String(10))
    complemento = db.Column(db.String(100))
    cidade = db.Column(db.String(100))
    estado = db.Column(db.String(100))
    envioSMS = db.Column(db.Boolean, default=False)
    adultoInapto = db.Column(db.Boolean, default=False)

