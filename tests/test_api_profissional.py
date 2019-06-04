from flask import url_for, current_app
from datetime import datetime
from tests.base_test import TestFlaskBase
from backend.models.profissional import Profissional


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
        profissional = self.create_profissional()
        response = self.client.get(url_for('profissional.profissional_cpf', cpf=profissional.cpf), headers=self.token)
        self.assertEqual(response.status_code, 200)

    def test_busca_profissional_por_cpf_errado(self):
        response = self.client.get(url_for('profissional.profissional_cpf', cpf='123'), headers=self.token)
        self.assertEqual(response.status_code, 404)

    def test_busca_profissional_por_cpf_vazio(self):
        response = self.client.get(url_for('profissional.profissional_cpf', cpf=''), headers=self.token)
        self.assertEqual(response.status_code, 404)

    def test_busca_lista_perfis_disponiveis(self):
        response = self.client.get(url_for('profissional.perfil'), headers=self.token)
        self.assertEqual(response.status_code, 200)

    def test_busca_lista_situacoes_disponiveis(self):
        response = self.client.get(url_for('profissional.situacao'), headers=self.token)
        self.assertEqual(response.status_code, 200)

    def test_busca_profissional_nome(self):
        profissional = self.create_profissional()
        response = self.client.get(url_for('profissional.profissional_nome', nome=profissional.nome), headers=self.token)
        self.assertEqual(response.status_code, 200)

    def test_busca_profissional_nome_parcial(self):
        profissional = self.create_profissional()
        response = self.client.get(url_for('profissional.profissional_nome', nome='profissional'), headers=self.token)
        self.assertEqual(response.status_code, 200)

    def test_busca_profissional_nome_errado(self):
        response = self.client.get(url_for('profissional.profissional_nome', nome='Texugo'), headers=self.token)
        self.assertEqual(response.status_code, 404)

    def test_busca_profissional_nome_vazio(self):
        response = self.client.get(url_for('profissional.profissional_nome', nome=''), headers=self.token)
        self.assertEqual(response.status_code, 404)

    def test_atualiza_um_profissional(self):
        profissional = self.create_profissional()
        profissional.nome = 'Novo nome'
        response = self.client.post(url_for('profissional.profissional_atualizar', nome=self.profissional_json['nome']), json=self.profissional_alterado, headers=self.token)
        self.assertEqual(response.status_code, 200)

    def test_atualiza_um_profissional_com_payload_vazio(self):
        response = self.client.post(url_for('profissional.profissional_atualizar', nome={}), json=self.profissional_alterado, headers=self.token)
        self.assertEqual(response.status_code, 404)

    def test_busca_profissional_nome_completo(self):
        profissional = self.create_profissional()
        response = self.client.get(url_for('profissional.profissional_nome_completo', nome=profissional.nome), headers=self.token)
        self.assertEqual(response.status_code, 200)

    def test_busca_profissional_nome_completo_nome_errado(self):
        response = self.client.get(url_for('profissional.profissional_nome_completo', nome='Texugo'), headers=self.token)
        self.assertEqual(response.status_code, 404)

    def test_reset_senha_de_user(self):
        profissional = self.create_profissional()
        senha_nova = {
            'id_profissional': str(profissional.id),
            'password': '54321'
        }
        response = self.client.post(url_for('profissional.profissional_reset_senha'), json=senha_nova, headers=self.token)
        self.assertEqual(response.status_code, 200)

    def test_reset_senha_de_user_com_campos_do_payload_vazio(self):
        senha_nova = {
            'id_profissional': '',
            'password': ''
        }
        response = self.client.post(url_for('profissional.profissional_reset_senha'), json=senha_nova, headers=self.token)
        self.assertEqual(response.status_code, 400)

    def test_reset_senha_de_user_com_payload_vazio(self):
        senha_nova = {}
        response = self.client.post(url_for('profissional.profissional_reset_senha'), json=senha_nova, headers=self.token)
        self.assertEqual(response.status_code, 400)

    def test_reset_senha_de_user_que_nao_existe(self):
        profissional = self.create_profissional()
        senha_nova = {
            'id_profissional': str(profissional.id + 100000),
            'password': '54321'
        }
        response = self.client.post(url_for('profissional.profissional_reset_senha'), json=senha_nova, headers=self.token)
        self.assertEqual(response.status_code, 404)
