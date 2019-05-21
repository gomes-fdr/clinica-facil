from unittest import TestCase
from flask import url_for, current_app
from json import loads
from backend import create_app
from backend.models.ps import PlanoSaude

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
        self.user = {
            'email': 'gomes.fdr@gmail.com',
            'password': '1234'
        }
        self.token = self.create_token()
        self.ps = 'teste'

    def tearDown(self):
        """
        Roda depois de todos os testes
        """
        # Apaga plano de saude testes
        PlanoSaude.query.filter_by(descricao=self.ps).delete()

        current_app.db.session.commit()

    def create_token(self):
        login = self.client.post(url_for('token.token'), json=self.user)
        return {
            'Authorization':
                'Bearer ' + loads(login.data.decode())['token']
}
