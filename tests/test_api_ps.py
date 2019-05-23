from flask import url_for
from tests.base_test import TestFlaskBase
from backend.models.paciente import Paciente

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

    def test_insere_um_ps_para_um_paciente_com_payload_vazio(self):
        self.client.post(url_for('paciente.paciente_novo'), json=self.paciente_json, headers=self.token)
        paciente = Paciente.query.filter_by(cpf=self.paciente_json['cpf']).first()

        response = self.client.post(url_for('plano_saude.post_ps_paciente'), json={}, headers=self.token)
        self.assertEqual(response.status_code, 400)


    