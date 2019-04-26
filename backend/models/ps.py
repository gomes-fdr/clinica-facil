from . import db
from backend.models.paciente import Paciente


class PlanoSaude(db.Model):
    """
    Planos de saúde disponíveis
    """
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100), nullable=False)

    @staticmethod
    def insere():
        planos = ('Particular','Unimed', 'Amil')

        for p in planos:
            ps = PlanoSaude.query.filter_by(descricao=p).first()
            if ps is None:
                ps = PlanoSaude(descricao = p)
                db.session.add(ps)
                db.session.commit()


class PlanoSaudePaciente(db.Model):
    """
    Plano de saúde Paciente
    """
    id = db.Column(db.Integer, primary_key=True)
    no_carteira = db.Column(db.String(50), nullable=False)
    dt_validade = db.Column(db.DateTime, nullable=False)

    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.id'))
    ps_id = db.Column(db.Integer, db.ForeignKey('plano_saude.id'))

    paciente = db.relationship('Paciente', backref='paciente')
    ps = db.relationship('PlanoSaude', backref='plano_saude')


    