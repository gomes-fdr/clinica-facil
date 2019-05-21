from flask import url_for
from tests.base_test import TestFlaskBase

class TestPS(TestFlaskBase):
    """
    Rotas para manipulação de Planos de Saúde
    """

    def test_pega_os_ps_cadastrados(self):
        response = self.client.get(url_for('plano_saude.get_ps'), headers=self.token)
        self.assertEqual(response.status_code, 200)

    def test_insere_um_novo_ps(self):
        response = self.client.post(url_for('plano_saude.post_ps', descricao=self.ps), headers=self.token)
        self.assertEqual(response.status_code, 201)

    def test_insere_um_ps_repetido(self):
        response = self.client.post(url_for('plano_saude.post_ps', descricao=self.ps), headers=self.token)
        response = self.client.post(url_for('plano_saude.post_ps', descricao=self.ps), headers=self.token)
        self.assertEqual(response.status_code, 400)
        self.assertEqual({'message': 'Plano de Saúde already in DB'}, response.json)

    