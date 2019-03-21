from werkzeug.security import generate_password_hash, check_password_hash

class User:

    def __init__(self, email, password):
        self.email = email
        self.password = generate_password_hash(password, hash='sha256')

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

    def to_dict(self):
        return user # tem que ser dicionário!!!

        
