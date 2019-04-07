from flask_marshmallow import Marshmallow
from marshmallow import fields
from marshmallow_sqlalchemy.fields import Related

from backend.models.paciente import Paciente
from backend.models.profissional import User
from backend.models.profissional import Profissional, Perfil, Situacao

ma = Marshmallow()

def configure(app):
    ma.init_app(app)

class UserSchema(ma.ModelSchema):
    class Meta:
        model = User

    email = fields.Str(required=True)
    password = fields.Str(required=True)


class PacienteSchema(ma.ModelSchema):
    class Meta:
        model = Paciente



class PerfilSchema(ma.ModelSchema):
    id = fields.Integer(dump_only=True)
    descricao = fields.Str()
    permissao = fields.Int()
    
    class Meta:
        model = Perfil
        fields = ('id', 'descricao', 'permissao')


class SituacaoSchema(ma.ModelSchema):
    id = fields.Integer(dump_only=True)
    descricao = fields.Str()
    
    class Meta:
        model = Situacao
        fields = ('id', 'descricao')


class ProfissionalSchema(ma.ModelSchema):
    perfil = fields.Nested(PerfilSchema)
    situacao = fields.Nested(SituacaoSchema)

    class Meta:
        model = Profissional
