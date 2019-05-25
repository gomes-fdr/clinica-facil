from datetime import datetime
from flask import url_for
from tests.base_test import TestFlaskBase
from backend.models.paciente import Paciente
from backend.models.ps import PlanoSaude, PlanoSaudePaciente

class TestPS(TestFlaskBase):
    """
    Rotas para manipulação de Planos de Saúde
    """

    def test_pega_os_ps_cadastrados(self):
        response = self.client.get(url_for('plano_saude.get_ps'), headers=self.token)
        self.assertEqual(response.status_code, 200)

    def test_insere_um_novo_ps(self):
        response = self.client.post(url_for('plano_saude.post_ps', descricao='Teste'), headers=self.token)
        self.assertEqual(response.status_code, 201)

    def test_insere_um_ps_repetido(self):
        response = self.client.post(url_for('plano_saude.post_ps', descricao='Teste'), headers=self.token)
        response = self.client.post(url_for('plano_saude.post_ps', descricao='Teste'), headers=self.token)
        self.assertEqual(response.status_code, 400)
        self.assertEqual({'message': 'Plano de Saúde already in DB'}, response.json)

    def test_insere_um_ps_para_um_paciente_com_payload_vazio(self):
        self.client.post(url_for('paciente.paciente_novo'), json=self.paciente_json, headers=self.token)
        paciente = Paciente.query.filter_by(cpf=self.paciente_json['cpf']).first()

        response = self.client.post(url_for('plano_saude.post_ps_paciente'), json={}, headers=self.token)
        self.assertEqual(response.status_code, 400)

    def test_insere_um_ps_para_um_paciente(self):
        self.client.post(url_for('paciente.paciente_novo'), json=self.paciente_json, headers=self.token)
        paciente = Paciente.query.filter_by(cpf=self.paciente_json['cpf']).first()

        self.client.post(url_for('plano_saude.post_ps', descricao='Teste'), headers=self.token)
        ps = PlanoSaude.query.filter_by(descricao='Teste').first()

        ps_json = {
            'ps': {
                'id': ps.id
            },
            'paciente_id': paciente.id,
            'no_carteira': 'teste-carteira',
            'dt_validade': str(datetime.strptime('24/05/2020', '%d/%m/%Y'))
        }
        response = self.client.post(url_for('plano_saude.post_ps_paciente'), json=ps_json, headers=self.token)
        self.assertEqual(response.status_code, 201)

    def test_insere_um_ps_para_um_paciente_repetindo_a_insercao_do_ps(self):
        self.client.post(url_for('paciente.paciente_novo'), json=self.paciente_json, headers=self.token)
        paciente = Paciente.query.filter_by(cpf=self.paciente_json['cpf']).first()

        self.client.post(url_for('plano_saude.post_ps', descricao='Teste'), headers=self.token)
        ps = PlanoSaude.query.filter_by(descricao='Teste').first()

        ps_json = {
            'ps': {
                'id': ps.id
            },
            'paciente_id': paciente.id,
            'no_carteira': 'teste-carteira',
            'dt_validade': str(datetime.strptime('24/05/2020', '%d/%m/%Y'))
        }
        response = self.client.post(url_for('plano_saude.post_ps_paciente'), json=ps_json, headers=self.token)
        response = self.client.post(url_for('plano_saude.post_ps_paciente'), json=ps_json, headers=self.token)
        self.assertEqual(response.status_code, 400)

    def test_busca_ps_de_um_paciente_que_nao_tem_ps(self):
        self.client.post(url_for('paciente.paciente_novo'), json=self.paciente_json, headers=self.token)
        paciente = Paciente.query.filter_by(cpf=self.paciente_json['cpf']).first()

        response = self.client.get(url_for('plano_saude.get_ps_paciente', paciente_id=paciente.id), headers=self.token)
        # import ipdb; ipdb.set_trace()
        self.assertEqual(response.status_code, 404)

    def test_busca_ps_de_um_paciente(self):
        self.client.post(url_for('paciente.paciente_novo'), json=self.paciente_json, headers=self.token)
        paciente = Paciente.query.filter_by(cpf=self.paciente_json['cpf']).first()
        self.client.post(url_for('plano_saude.post_ps', descricao='Teste'), headers=self.token)
        ps = PlanoSaude.query.filter_by(descricao='Teste').first()

        ps_json = {
            'ps': {
                'id': ps.id
            },
            'paciente_id': paciente.id,
            'no_carteira': 'teste-carteira',
            'dt_validade': str(datetime.strptime('24/05/2020', '%d/%m/%Y'))
        }
        response = self.client.post(url_for('plano_saude.post_ps_paciente'), json=ps_json, headers=self.token)

        response = self.client.get(url_for('plano_saude.get_ps_paciente', paciente_id=paciente.id), headers=self.token)
        # import ipdb; ipdb.set_trace()
        self.assertEqual(response.status_code, 200)

    def test_apaga_ps_de_um_paciente(self):
        self.client.post(url_for('paciente.paciente_novo'), json=self.paciente_json, headers=self.token)
        paciente = Paciente.query.filter_by(cpf=self.paciente_json['cpf']).first()
        self.client.post(url_for('plano_saude.post_ps', descricao='Teste'), headers=self.token)
        ps = PlanoSaude.query.filter_by(descricao='Teste').first()

        ps_json = {
            'ps': {
                'id': ps.id
            },
            'paciente_id': paciente.id,
            'no_carteira': 'teste-carteira',
            'dt_validade': str(datetime.strptime('24/05/2020', '%d/%m/%Y'))
        }
        response = self.client.post(url_for('plano_saude.post_ps_paciente'), json=ps_json, headers=self.token)
        ps_paciente = PlanoSaudePaciente.query.filter_by(no_carteira=ps_json['no_carteira']).first()

        response = self.client.get(url_for('plano_saude.delete_ps_paciente', id=ps_paciente.id), headers=self.token)
        # import ipdb; ipdb.set_trace()
        self.assertEqual(response.status_code, 200)

    def test_apaga_ps_que_nao_existe_de_um_paciente(self):
        self.client.post(url_for('paciente.paciente_novo'), json=self.paciente_json, headers=self.token)
        paciente = Paciente.query.filter_by(cpf=self.paciente_json['cpf']).first()
        self.client.post(url_for('plano_saude.post_ps', descricao='Teste'), headers=self.token)
        ps = PlanoSaude.query.filter_by(descricao='Teste').first()

        ps_json = {
            'ps': {
                'id': ps.id
            },
            'paciente_id': paciente.id,
            'no_carteira': 'teste-carteira',
            'dt_validade': str(datetime.strptime('24/05/2020', '%d/%m/%Y'))
        }
        response = self.client.post(url_for('plano_saude.post_ps_paciente'), json=ps_json, headers=self.token)
        ps_paciente = PlanoSaudePaciente.query.filter_by(no_carteira=ps_json['no_carteira']).first()

        response = self.client.get(url_for('plano_saude.delete_ps_paciente', id=ps_paciente.id+10), headers=self.token)
        # import ipdb; ipdb.set_trace()
        self.assertEqual(response.status_code, 404)



    