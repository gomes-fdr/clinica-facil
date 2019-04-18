from . import db
from backend.models.paciente import Paciente
from backend.models.profissional import Profissional


class ProntuarioLegado(db.Model):
    """
    Prontuarios do sistema legado
    """
    id = db.Column(db.Integer, primary_key=True)
    conteudo = db.Column(db.Text)

    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.id'))