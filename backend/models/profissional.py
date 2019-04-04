from . import db
from werkzeug.security import check_password_hash, generate_password_hash

class Permissao:
    """
    Permissões para grupos de usuários
    v_ = VISUALIZA
    E_ = EDITA
    """
    ADM_SISTEMA     = 65535             # 1111 1111  1111 1111
    COORD_USUARIOS  = 1                 # 0000 0000  0000 0001  
    V_AGENDA        = 2                 # 0000 0000  0000 0010  
    E_AGENDA        = 4                 # 0000 0000  0000 0100 
    COORD_AGENDA    = 8                 # 0000 0000  0000 1000  
    V_PRONTUARIO    = 16                # 0000 0000  0001 0000
    E_PRONTUARIO    = 32                # 0000 0000  0010 0000
    V_FINANCAS      = 64                # 0000 0000  0100 0000 
    E_FINANCAS      = 128               # 0000 0000  1000 0000 
    V_DOC_ORDINARIO = 256               # 0000 0001  0000 0000
    E_DOC_ORDINARIO = 512               # 0000 0010  0000 0000
    V_DOC_SENSIVEL  = 1024              # 0000 0100  0000 0000
    E_DOC_SENSIVEL  = 2048              # 0000 1000  0000 0000


class Perfil(db.Model):
    """
    Perfil dos coloboradores da clinica
    """
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100))
    permissao = db.Column(db.Integer)

    profissionais = db.relationship('Profissional', backref='perfil', lazy='dynamic')

    @staticmethod
    def insere():
        perfis = {
            'Administracao': (Permissao.ADM_SISTEMA)
            'Cliente': (),
            'Recepção': (),
            'Psicólogo': (),
            'Psiquiatra': (),
            'Nutricionista': (),
            'Fonoaudiólogo': (),
            'Neurologista': (),
            'Financeiro': (),
            'Coordenador-Agendas': (),
        }
        for p in perfis:
            perfil = Perfil.query.filter_by(descricao=p).first()
            if perfil is None:
                perfil = Perfil(descricao = p)
            perfil.permissao = perfis[p]
            db.session.add(perfil)
        db.session.commit()



class Situacao(db.Model):
    """
    Situação dos coloboradores da clinica
    """
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100))

    profissionais = db.relationship('Profissional', backref='situacao')

    def __repr__(self):
        return '{}'.format(self.descricao)

    @staticmethod
    def insere():
        situacoes = ['Inativo', 'Ativo', 'Atestado', 'Ferias', 'Desligado']
        for s in situacoes:
            situacao = Situacao.query.filter_by(descricao=s).first()
            if situacao is None:
                situacao = Situacao(descricao = s)
            db.session.add(situacao)
        db.session.commit()


class User(db.Model):
    """
    Usuários do sistema
    """
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    perfil_id = db.Column(db.Integer, db.ForeignKey('perfil.id'))

    @staticmethod
    def insere():
        """Insere usuário administrador do sistema"""
        pass

    def __init__(self, email, password):
        self.email = email
        self.password = generate_password_hash(password)

    def gen_hash(self):
        self.password = generate_password_hash(self.password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)



class Profissional(db.Model):
    """
    Profissionais que atuam na clinica
    """
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100))
    dt_nascimento = db.Column(db.DateTime, nullable=False)
    cpf = db.Column(db.String(11), index=True, unique=True, nullable=False)
    rg = db.Column(db.String(10), unique=True)
    faculdade = db.Column(db.String(100), nullable=False)
    no_conselho = db.Column(db.String(100))
    t_celular = db.Column(db.String(20))
    t_fixo = db.Column(db.String(20))
    cep = db.Column(db.String(15))
    rua = db.Column(db.String(100), nullable=False)
    numero = db.Column(db.String(10), nullable=False)
    complemento = db.Column(db.String(100))
    cidade = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.String(100), nullable=False)

    perfil_id = db.Column(db.Integer, db.ForeignKey('perfil.id'))
    situacao_id = db.Column(db.Integer, db.ForeignKey('situacao.id'))


