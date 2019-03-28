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
        return check_password_hash(password, self.password)

    def __init__(self, email, password):
        self.email = email
        self.password = generate_password_hash(password)

    @classmethod
    def autorizar(cls, **kwargs):
    # def autorizar(**kwargs):
        email = kwargs.get('email')
        password = kwargs.get('password')

        if not email or not password:
            return None

        # user = cls.query.filter_by(email=email).first()
        user = {'id': '1', 'email': 'recepcao@clinicadarmas.com.br', 'password': '1234'}
        print(user.get('password'))

        # if not user or not check_password_hash((user['password']), password):
        if not user or (user.get('password') != str(password)) or (user.get('email') != email):
            return None

        return user



        
