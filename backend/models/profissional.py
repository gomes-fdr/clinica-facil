from . import db
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
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
    is_especialista = db.Column(db.Boolean, default=True)

    profissionais = db.relationship('Profissional', backref='perfil', lazy='dynamic')

    @staticmethod
    def insere():
        perfis = {
            'Administracao': (Permissao.ADM_SISTEMA),
            'Recepcao': (
                Permissao.V_AGENDA |
                Permissao.E_AGENDA
            ),
            'Psicologo': (
                Permissao.V_AGENDA |
                Permissao.E_AGENDA |
                Permissao.V_PRONTUARIO |
                Permissao.E_PRONTUARIO
            ),
            'Psiquiatra': (
                Permissao.V_AGENDA |
                Permissao.E_AGENDA |
                Permissao.V_PRONTUARIO |
                Permissao.E_PRONTUARIO
            ),
            'Nutricionista': (
                Permissao.V_AGENDA |
                Permissao.E_AGENDA |
                Permissao.V_PRONTUARIO |
                Permissao.E_PRONTUARIO
            ),
            'Fonoaudiologo': (
                Permissao.V_AGENDA |
                Permissao.E_AGENDA |
                Permissao.V_PRONTUARIO |
                Permissao.E_PRONTUARIO
            ),
            'Neurologista': (
                Permissao.V_AGENDA |
                Permissao.E_AGENDA |
                Permissao.V_PRONTUARIO |
                Permissao.E_PRONTUARIO
            ),
            'Coordenador-Agendas': (
                Permissao.COORD_AGENDA |
                Permissao.V_AGENDA |
                Permissao.E_AGENDA |
                Permissao.V_PRONTUARIO |
                Permissao.E_PRONTUARIO
            ),
        }
        for p in perfis:
            perfil = Perfil.query.filter_by(descricao=p).first()
            if perfil is None:
                perfil = Perfil(descricao = p)
            perfil.permissao = perfis[p]
            db.session.add(perfil)
        db.session.commit()

    def __repr__(self):
        return '{}'.format(self.descricao)



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

    def __repr__(self):
        return '{}'.format(self.descricao)


class User(db.Model):
    """
    Usuários do sistema
    """
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return 'email: {}'.format(self.email)

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
    email = db.Column(db.String(100), nullable=False, unique=True)
    dt_nascimento = db.Column(db.DateTime)
    cpf = db.Column(db.String(11), index=True, unique=True)
    rg = db.Column(db.String(10), unique=True)
    faculdade = db.Column(db.String(100))
    no_conselho = db.Column(db.String(100))
    t_celular = db.Column(db.String(20))
    t_fixo = db.Column(db.String(20))
    cep = db.Column(db.String(15))
    rua = db.Column(db.String(100))
    numero = db.Column(db.String(10))
    complemento = db.Column(db.String(100))
    cidade = db.Column(db.String(100))
    estado = db.Column(db.String(100))

    perfil_id = db.Column(db.Integer, db.ForeignKey('perfil.id'))
    situacao_id = db.Column(db.Integer, db.ForeignKey('situacao.id'))

    perfis = db.relationship("Perfil", backref=db.backref("perfil", lazy="dynamic"))
    situacoes = db.relationship("Situacao", backref=db.backref("situacao", lazy="dynamic"))

    def __repr__(self):
        return 'Nome: {}, perfil: {}, situação: {}'.format(self.nome, self.perfil, self.situacao)

    @staticmethod
    def insere_adm():

        try:
            perfil = Perfil.query.filter_by(descricao='Administracao').first()
        except SQLAlchemyError as e:
                error = str(e.__dict__['orig'])

        try:
            situacao = Situacao.query.filter_by(descricao='Ativo').first()
        except SQLAlchemyError as e:
                error = str(e.__dict__['orig'])

        try:
            adm = Profissional(nome='Fabiano da Rosa Gomes', email='gomes.fdr@gmail.com', 
                            dt_nascimento=datetime(1974, 5, 24), cpf='60976900025', faculdade='Senac', rua='Silvério Souto',
                            numero='380', cidade='Porto Alegre', estado='RS', perfil=perfil, situacao=situacao)
        except SQLAlchemyError as e:
                error = str(e.__dict__['orig'])

        db.session.add(adm)
        db.session.commit()
        return adm

    def create_user(self, profissional):
        try:
            user = User(email=profissional.email, password='1234')
        except SQLAlchemyError as e:
                error = str(e.__dict__['orig'])

        db.session.add(user)
        db.session.commit()

    def update_user(self, profissional):
        try:
            user = User.query.filter_by(email=profissional.email).first()
            # user.email = profissional_novo.email
        except SQLAlchemyError as e:
                error = str(e.__dict__['orig'])

        db.session.commit()

    
    def update_password(self, profissional, password):
        try:
            user = User.query.filter_by(email=profissional.email).first()
            user.password = password
            user.gen_hash()
        except SQLAlchemyError as e:
                error = str(e.__dict__['orig'])

        db.session.commit()






