from flask import url_for
from tests.base_test import TestFlaskBase

class TestToken(TestFlaskBase):
    """
    Rotas para obtenção de token de autenticação
    """
    def test_token_s_payload(self):
        data = {}
        response = self.client.post(url_for('token.token'), json=data)
        self.assertEqual(response.status_code, 401)

    def test_token_user_errado(self):
        data = {
            'email': 'abobrinha@gmail.com',
            'password': 'bla'
        }
        response = self.client.post(url_for('token.token'), json=data)
        self.assertEqual(response.status_code, 401)

    def test_token_payload_vazio(self):
        data = {
            'email': '',
            'password': ''
        }
        response = self.client.post(url_for('token.token'), json=data)
        self.assertEqual(response.status_code, 401)

    def test_token_c_usuario_e_senha_correto(self):
        data = {
            'email': 'gomes.fdr@gmail.com',
            'password': '1234'
        }
        # import ipdb; ipdb.set_trace()
        response = self.client.post(url_for('token.token'), json=data)

        self.assertEqual(response.status_code, 200)

    def test_token_c_credencial_invalida(self):
        data = {
            'email': 'biancaferraz@clinicadarmas.com.br',
            'password': '1234'
        }
        # import ipdb; ipdb.set_trace()
        response = self.client.post(url_for('token.token'), json=data)

        self.assertEqual(response.status_code, 401)