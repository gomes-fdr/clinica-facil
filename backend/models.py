from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def configure(app):
    db.init_app(app)
    app.db = db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def gen_hash(self):
        self.password = generate_password_hash(self.password)

    def verify_password(self, password):
        return check_password_hash(str(self.password), password)

    def __init__(self, email, password):
        self.email = email
        self.password = generate_password_hash(password)
        
