import os

from flask import Flask, jsonify, render_template
from flask_cors import CORS
from flask_migrate import Migrate

from .models import configure as config_db
from .paciente import bp_paciente
from .profissional import bp_profissional
from .serealizer import configure as config_ma
from .token import bp_token
from .user import bp_user
from .prontuario import bp_prontuario
from .ps import bp_ps
from .agenda import bp_agenda
from .tasks.task_sms import bp_task_sms

from flask_jwt_extended import JWTManager
from flask_executor import Executor

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
    app.executor = Executor(app)
    Migrate(app, app.db)
    JWTManager(app)

    app.register_blueprint(bp_user)
    app.register_blueprint(bp_token)
    app.register_blueprint(bp_paciente)
    app.register_blueprint(bp_profissional)
    app.register_blueprint(bp_prontuario)
    app.register_blueprint(bp_ps)
    app.register_blueprint(bp_agenda)

    # TODO: taks Envio diário de SMS
    # TODO: taks Data final de horarios(emitir aviso de que chegou ao fim)
    # TODO: taks Agendas canceladas
    # TODO: task Encaminhar paciente para o profissional
    app.register_blueprint(bp_task_sms)

    return app