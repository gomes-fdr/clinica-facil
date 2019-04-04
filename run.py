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

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")
