from flask import url_for
from tests.base_test import TestFlaskBase

class TestUser(TestFlaskBase):
    """
    Rotas para manipular Users
    """

    def test_cria_um_usuario(self):
        user = {
            'email': self.paciente_json['email'],
            'password': '1234'
        }
        response = self.client.post(url_for('user.register'), json=user, headers=self.token)
        self.assertEqual(response.status_code, 201)

    def test_cria_um_usuario_com_payload_vazio(self):
        user = {}
        response = self.client.post(url_for('user.register'), json=user, headers=self.token)
        self.assertEqual(response.status_code, 401)
