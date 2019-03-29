import os
from flask import Flask, render_template, jsonify
from flask_migrate import Migrate
from flask_cors import CORS

from backend.models import configure as config_db
from backend.serealizer import configure as config_ma

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

from backend import bp as api
app.register_blueprint(api)

from backend.user import bp_user
app.register_blueprint(bp_user)

from backend.token import bp_token
app.register_blueprint(bp_token)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")
