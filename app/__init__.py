from flask import Flask

def create_app():
    app = Flask(__name__, static_url_path='')

    from app.core import bp as core_bp
    app.register_blueprint(core_bp)

    return app