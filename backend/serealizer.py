from marshmallow import fields, validates, ValidationError
from flask_marshmallow import Marshmallow
from .models import User

ma = Marshmallow()

def configure(app):
    ma.init_app(app)

class UserSchema(ma.ModelSchema):
    class Meta:
        model = User

    email = fields.Str(required=True)
    password = fields.Str(required=True)