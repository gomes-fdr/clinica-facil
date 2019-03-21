from flask import Flask, render_template, jsonify
from random import *
from flask_cors import CORS

app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./dist")
app.config['JSON_SORT_KEYS'] = False
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")

from backend import bp as api
app.register_blueprint(api)