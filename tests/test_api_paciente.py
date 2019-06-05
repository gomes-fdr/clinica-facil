from flask import url_for
from datetime import datetime
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
        self.assertEqual(response.status_code, 400)

    def test_atualiza_um_paciente(self):
        paciente = self.create_paciente()
        paciente.nome = 'Nome alterado'
        response = self.client.post(url_for('paciente.paciente_atualizar', cpf=paciente.cpf), json=self.paciente_alterado, headers=self.token)
        self.assertEqual(response.status_code, 200)
        
    def test_atualiza_um_paciente_com_payload_vazio(self):
        paciente = self.create_paciente()
        response = self.client.post(url_for('paciente.paciente_atualizar', cpf=paciente.cpf), json={}, headers=self.token)
        self.assertEqual(response.status_code, 400)

    def test_atualiza_um_paciente_com_cpf_vazio(self):
        response = self.client.post(url_for('paciente.paciente_atualizar', cpf=''), json=self.paciente_alterado, headers=self.token)
        self.assertEqual(response.status_code, 404)
        
    def test_atualiza_um_paciente_com_cpf_errado(self):
        response = self.client.post(url_for('paciente.paciente_atualizar', cpf='123'), json=self.paciente_alterado, headers=self.token)
        self.assertEqual(response.status_code, 400)

    def test_busca_um_paciente_por_cpf(self):
        paciente = self.create_paciente()
        response = self.client.get(url_for('paciente.paciente_cpf', cpf=paciente.cpf), headers=self.token)
        # import ipdb; ipdb.set_trace()
        self.assertEqual(response.status_code, 200)
        
    def test_busca_um_paciente_por_cpf_errado(self):
        response = self.client.get(url_for('paciente.paciente_cpf', cpf='123'), headers=self.token)
        # import ipdb; ipdb.set_trace()
        self.assertEqual(response.status_code, 404)
        
    def test_busca_um_paciente_por_nome(self):
        paciente = self.create_paciente()
        response = self.client.get(url_for('paciente.paciente_nome', nome=paciente.nome), headers=self.token)
        # import ipdb; ipdb.set_trace()
        self.assertEqual(response.status_code, 200)
        
    def test_busca_um_paciente_por_parte_do_nome(self):
        paciente = self.create_paciente()
        response = self.client.get(url_for('paciente.paciente_nome', nome=paciente.nome.split(' ')[0]), headers=self.token)
        # import ipdb; ipdb.set_trace()
        self.assertEqual(response.status_code, 200)
        
    def test_busca_um_paciente_por_nome_que_nao_existe(self):
        response = self.client.get(url_for('paciente.paciente_nome', nome='Texugo'), headers=self.token)
        # import ipdb; ipdb.set_trace()
        self.assertEqual(response.status_code, 404)

    def test_busca_um_paciente_por_nome_completo(self):
        paciente = self.create_paciente()
        response = self.client.get(url_for('paciente.paciente_nome_completo', nome=paciente.nome), headers=self.token)
        # import ipdb; ipdb.set_trace()
        self.assertEqual(response.status_code, 200)

    def test_busca_um_paciente_por_nome_completo_que_nao_existe(self):
        response = self.client.get(url_for('paciente.paciente_nome_completo', nome='Texugo'), headers=self.token)
        # import ipdb; ipdb.set_trace()
        self.assertEqual(response.status_code, 404)
        
