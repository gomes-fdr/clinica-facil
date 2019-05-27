from flask import url_for
from tests.base_test import TestFlaskBase
from backend.models.paciente import Paciente

class TestProntuarioLegado(TestFlaskBase):
    """
    Rotas para manipular o prontuário legado
    """

    def test_pega_os_prontuarios_de_uma_paciente_que_nao_tem_prontuario(self):
        self.client.post(url_for('paciente.paciente_novo'), json=self.paciente_json, headers=self.token)
        paciente = Paciente.query.filter_by(cpf=self.paciente_json['cpf']).first()

        response = self.client.get(url_for('prontuario.prontuario_leg_paciente', paciente_id=paciente.id), headers=self.token)
        self.assertEqual(response.status_code, 404)