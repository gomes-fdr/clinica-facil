from . import db

class Cid(db.Model):
    """
    LISTA CID-10 - A Classificação Internacional de Doenças e Problemas Relacionados à Saúde 
    Retirado da API:
    https://cid-api.herokuapp.com/
    Em 07/05/2019
    """
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(15))
    nome = db.Column(db.String(256))