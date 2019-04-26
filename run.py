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

app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./dist")
            
app.config['JSON_SORT_KEYS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

config_db(app)
config_ma(app)
Migrate(app, app.db)

app.register_blueprint(bp_user)
app.register_blueprint(bp_token)
app.register_blueprint(bp_paciente)
app.register_blueprint(bp_profissional)
app.register_blueprint(bp_prontuario)
app.register_blueprint(bp_ps)
app.register_blueprint(bp_agenda)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")

# TODO: Criar estrutura para logar eventos importantes
