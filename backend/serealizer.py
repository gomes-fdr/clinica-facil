from flask_marshmallow import Marshmallow
from marshmallow import fields
from marshmallow_sqlalchemy.fields import Related

from backend.models.paciente import Paciente
from backend.models.profissional import User
from backend.models.profissional import Profissional, Perfil, Situacao
from backend.models.prontuario import ProntuarioLegado
from backend.models.ps import PlanoSaude, PlanoSaudePaciente
from backend.models.agenda import (Local, Horario, Consulta)

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


class PacienteSchema2(ma.ModelSchema):
    class Meta:
        model = Paciente
        fields = [('nome')]



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


class ProntuarioLegadoSchema(ma.ModelSchema):
    paciente = fields.Nested(PacienteSchema)

    class Meta:
        model = ProntuarioLegado

class PlanoSaudeSchema(ma.ModelSchema):
    class Meta:
        model = PlanoSaude

class PlanoSaudeSchema2(ma.ModelSchema):
    class Meta:
        model = PlanoSaude
        fields = [('descricao')]


class PlanoSaudePacienteSchema(ma.ModelSchema):
    paciente = fields.Nested(PacienteSchema2)
    ps = fields.Nested(PlanoSaudeSchema2)

    class Meta:
        model = PlanoSaudePaciente
        fields = ('id','no_carteira', 'dt_validade', 'ps', 'paciente')


class LocalSchema(ma.ModelSchema):
    class Meta:
        model = Local
        fields = ('id', 'descricao')


class HorarioSchema(ma.ModelSchema):
    class Meta:
        model = Horario


class ConsultaSchema(ma.ModelSchema):
    class Meta:
        model = Consulta