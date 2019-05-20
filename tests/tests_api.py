from unittest import TestCase
from flask import url_for
from backend import create_app

class TestFlaskBase(TestCase):
    def setUp(self):
        """
        Roda antes de todos os testes.
        """
        self.app = create_app()
    
        # Configurando o APP para testes (live de pytohn #81)
        self.app.config.testing = True                      # Coloca o APP em teste
        self.app_context = self.app.test_request_context()  # Pede um contexto para testes
        self.app_context.push()                             # Coloca o App no contexto de testes
        self.client = self.app.test_client()                # Dá Acesso aos requests usando with

    def tearDown(self):
        """
        Roda depois de todos os testes
        """

class TestToken(TestFlaskBase):
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