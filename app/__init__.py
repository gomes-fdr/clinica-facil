from flask import Flask, render_template
from flask_cors import CORS

def create_app():
    app = Flask(__name__, static_url_path='')
    app.config['JSON_SORT_KEYS'] = False
    CORS(app)

    from app.core import bp as core_bp
    app.register_blueprint(core_bp)

    return app