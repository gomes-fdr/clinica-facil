from flask_marshmallow import Marshmallow
from marshmallow import fields
from marshmallow_sqlalchemy.fields import Related

from backend.models.paciente import Paciente
from backend.models.profissional import User
from backend.models.profissional import Profissional, Perfil, Situacao
from backend.models.prontuario import ProntuarioLegado
from backend.models.ps import PlanoSaude, PlanoSaudePaciente
from backend.models.agenda import (Local, Horario, Consulta)
from backend.models.cid import Cid

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


class ProfissionalSchema2(ma.ModelSchema):
    perfil = fields.Nested(PerfilSchema)
    situacao = fields.Nested(SituacaoSchema)

    class Meta:
        model = Profissional
        fields=('id', 'nome')


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
    # Necessário para sobrepor o 'backref' em models
    # Serve tb para alterar o nome do atributo na saida do json
    # profissional_id = fields.Number(attribute="profissional_id")
    # local_id = fields.Number(attribute="local_id")
    profissional = fields.Nested(ProfissionalSchema2)
    local = fields.Nested(LocalSchema)

    class Meta:
        model = Horario
        # fields = ('livre', 'profissional_id',  'local_id', 'profissional_id', 'hora_fim', 'duracao', 'dt_dia', 'id', 'hora_ini')



class ConsultaSchema(ma.ModelSchema):
    horario = fields.Nested(HorarioSchema)
    paciente = fields.Nested(PacienteSchema)
    plano_saude_paciente = fields.Nested(PlanoSaudePacienteSchema)
    class Meta:
        model = Consulta


class CidSchema(ma.ModelSchema):
    class Meta:
        model = Cid