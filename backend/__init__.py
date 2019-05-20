import os

from flask import Flask, jsonify, render_template
from flask_cors import CORS
from flask_migrate import Migrate

from backend.models import configure as config_db
from backend.paciente import bp_paciente
from backend.profissional import bp_profissional
from backend.serealizer import configure as config_ma
from backend.token import bp_token
from backend.user import bp_user
from backend.prontuario import bp_prontuario
from backend.ps import bp_ps
from backend.agenda import bp_agenda

from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__)

    app.static_folder = "../dist/static"
    app.template_folder = "../dist"

    app.config['JSON_SORT_KEYS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'Batatinhas voadoras são melhores que eu, dulossauro!'
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    config_db(app)
    config_ma(app)
    Migrate(app, app.db)
    JWTManager(app)

    app.register_blueprint(bp_user)
    app.register_blueprint(bp_token)
    app.register_blueprint(bp_paciente)
    app.register_blueprint(bp_profissional)
    app.register_blueprint(bp_prontuario)
    app.register_blueprint(bp_ps)
    app.register_blueprint(bp_agenda)

    return app