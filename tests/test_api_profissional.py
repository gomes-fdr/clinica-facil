from flask import url_for
from datetime import datetime
from tests.base_test import TestFlaskBase

class TestProfissional(TestFlaskBase):
    """
    Rotas para manipulação de Profissionais
    """
    def test_insere_um_profissional(self):
        response = self.client.post(url_for('profissional.profissional'), json=self.profissional_json, headers=self.token)
        # import ipdb; ipdb.set_trace()
        self.assertEqual(response.status_code, 201)

    def test_insere_um_profissional_c_payload_vazio(self):
        response = self.client.post(url_for('profissional.profissional'), json={}, headers=self.token)
        # import ipdb; ipdb.set_trace()
        self.assertEqual(response.status_code, 400)

    def test_busca_profissional_por_cpf(self):
        self.client.post(url_for('profissional.profissional'), json=self.profissional_json, headers=self.token)
        response = self.client.get(url_for('profissional.profissional_cpf', cpf=self.profissional_json['cpf']), headers=self.token)
        self.assertEqual(response.status_code, 200)

    def test_busca_profissional_por_cpf_errado(self):
        self.client.post(url_for('profissional.profissional'), json=self.profissional_json, headers=self.token)
        response = self.client.get(url_for('profissional.profissional_cpf', cpf='123'), headers=self.token)
        self.assertEqual(response.status_code, 404)

    def test_busca_profissional_por_cpf_vazio(self):
        self.client.post(url_for('profissional.profissional'), json=self.profissional_json, headers=self.token)
        response = self.client.get(url_for('profissional.profissional_cpf', cpf=''), headers=self.token)
        self.assertEqual(response.status_code, 404)

    def test_busca_lista_perfis_disponiveis(self):
        response = self.client.get(url_for('profissional.perfil'), headers=self.token)
        self.assertEqual(response.status_code, 200)

    def test_busca_lista_situacoes_disponiveis(self):
        response = self.client.get(url_for('profissional.situacao'), headers=self.token)
        self.assertEqual(response.status_code, 200)

    def test_busca_profissional_nome(self):
        self.client.post(url_for('profissional.profissional'), json=self.profissional_json, headers=self.token)
        response = self.client.get(url_for('profissional.profissional_nome', nome=self.profissional_json['nome']), headers=self.token)
        self.assertEqual(response.status_code, 200)

    def test_busca_profissional_nome_parcial(self):
        self.client.post(url_for('profissional.profissional'), json=self.profissional_json, headers=self.token)
        response = self.client.get(url_for('profissional.profissional_nome', nome='profissional'), headers=self.token)
        self.assertEqual(response.status_code, 200)

    def test_busca_profissional_nome_errado(self):
        self.client.post(url_for('profissional.profissional'), json=self.profissional_json, headers=self.token)
        response = self.client.get(url_for('profissional.profissional_nome', nome='Texugo'), headers=self.token)
        self.assertEqual(response.status_code, 404)

    def test_busca_profissional_nome_vazio(self):
        self.client.post(url_for('profissional.profissional'), json=self.profissional_json, headers=self.token)
        response = self.client.get(url_for('profissional.profissional_nome', nome=''), headers=self.token)
        self.assertEqual(response.status_code, 404)

    def test_atualiza_um_profissional(self):
        self.client.post(url_for('profissional.profissional'), json=self.profissional_json, headers=self.token)
        response = self.client.post(url_for('profissional.profissional_atualizar', nome=self.profissional_json['nome']), json=self.profissional_alterado, headers=self.token)
        self.assertEqual(response.status_code, 200)

