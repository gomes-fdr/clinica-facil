from flask_marshmallow import Marshmallow
from marshmallow import ValidationError, fields, validates

from backend.models.paciente import Paciente
from backend.models.profissional import User

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
