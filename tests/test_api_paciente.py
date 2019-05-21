from flask import url_for
from tests.base_test import TestFlaskBase

class TestPaciente(TestFlaskBase):
    """
    Rotas para manipulação de Pacientes
    """
    def test_cria_um_paciente_para_testes(self):
        response = self.client.post(url_for('paciente.paciente_novo'), json=self.paciente_json, headers=self.token)
        # import ipdb; ipdb.set_trace()
        self.assertEqual(response.status_code, 201)

    def test_criacao_paciente_apartir_de_json_vazio(self):
        response = self.client.post(url_for('paciente.paciente_novo'), json={}, headers=self.token)

        self.assertEqual(response.status_code, 404)
