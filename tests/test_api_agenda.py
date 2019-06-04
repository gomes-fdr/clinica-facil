from datetime import datetime
from flask import url_for
from tests.base_test import TestFlaskBase

from backend.models.agenda import Local, Horario
from backend.models.profissional import (Profissional, Perfil)
from backend.models.ps import PlanoSaude, PlanoSaudePaciente

class TestAgenda(TestFlaskBase):
    """
    Rotas para manipular Agenda
    """

    def test_busca_sala_atendimento(self):
        response = self.client.get(url_for('agenda.get_sala'), headers=self.token)
        self.assertEqual(response.status_code, 200)

    def test_adiciona_sala_atendimento(self):
        response = self.client.post(url_for('agenda.post_sala', descricao='sala teste'), headers=self.token)
        self.assertEqual(response.status_code, 201)

    def test_adiciona_sala_atendimento_repetida(self):
        response = self.client.post(url_for('agenda.post_sala', descricao='sala teste'), headers=self.token)
        response = self.client.post(url_for('agenda.post_sala', descricao='sala teste'), headers=self.token)
        self.assertEqual(response.status_code, 400)

    def test_adiciona_sala_atendimento(self):
        self.client.post(url_for('agenda.post_sala', descricao='sala teste'), headers=self.token)
        local = Local.query.filter_by(descricao='sala teste').first()
        profissional = self.create_profissional()

        horario = { 
            'date': datetime.strptime('24/05/2050', '%d/%m/%Y'), 
            'startTime': '11:00', 
            'endTime': '11:45', 
            'livre': True, 
            'local_id': local.id, 
            'profissional_id': profissional.id, 
            'duracao': 45
        } 
        response = self.client.post(url_for('agenda.post_horario'), json=horario, headers=self.token)
        self.assertEqual(response.status_code, 201)

    def test_adiciona_sala_atendimento_repetido(self):
        self.client.post(url_for('agenda.post_sala', descricao='sala teste'), headers=self.token)
        local = Local.query.filter_by(descricao='sala teste').first()
        profissional = self.create_profissional()

        horario = { 
            'date': datetime.strptime('24/05/2050', '%d/%m/%Y'), 
            'startTime': '11:00', 
            'endTime': '11:45', 
            'livre': True, 
            'local_id': local.id, 
            'profissional_id': profissional.id, 
            'duracao': 45
        } 
        self.client.post(url_for('agenda.post_horario'), json=horario, headers=self.token)
        response = self.client.post(url_for('agenda.post_horario'), json=horario, headers=self.token)
        self.assertEqual(response.status_code, 409)

    def test_busca_horario_de_um_profissional(self):
        self.client.post(url_for('agenda.post_sala', descricao='sala teste'), headers=self.token)
        local = Local.query.filter_by(descricao='sala teste').first()
        profissional = self.create_profissional()

        horario = { 
            'date': datetime.strptime('24/05/2050', '%d/%m/%Y'), 
            'startTime': '11:00', 
            'endTime': '11:45', 
            'livre': True, 
            'local_id': local.id, 
            'profissional_id': profissional.id, 
            'duracao': 45
        } 
        self.client.post(url_for('agenda.post_horario'), json=horario, headers=self.token)
        response = self.client.get(url_for('agenda.get_horario_profissional',
            selecao='profissional',
            dt_inicio='23/05/2050',
            dt_fim = '24/05/2050',
            livre = 'true',
            profissional_id=profissional.id), headers=self.token)
        # import ipdb; ipdb.set_trace()
        self.assertEqual(response.status_code, 200)
        
    def test_busca_horario_de_todos_profissional(self):
        self.client.post(url_for('agenda.post_sala', descricao='sala teste'), headers=self.token)
        local = Local.query.filter_by(descricao='sala teste').first()
        profissional = self.create_profissional()

        horario = { 
            'date': datetime.strptime('24/05/2050', '%d/%m/%Y'), 
            'startTime': '11:00', 
            'endTime': '11:45', 
            'livre': True, 
            'local_id': local.id, 
            'profissional_id': profissional.id, 
            'duracao': 45
        } 
        self.client.post(url_for('agenda.post_horario'), json=horario, headers=self.token)
        response = self.client.get(url_for('agenda.get_horario_profissional',
            selecao='profissional',
            dt_inicio='23/05/2050',
            dt_fim = '24/05/2050',
            livre = 'true',
            profissional_id='*'), headers=self.token)
        # import ipdb; ipdb.set_trace()
        self.assertEqual(response.status_code, 200)
        
    def test_busca_horario_de_todos_profissional_por_especialidade(self):
        self.client.post(url_for('agenda.post_sala', descricao='sala teste'), headers=self.token)
        local = Local.query.filter_by(descricao='sala teste').first()
        profissional = self.create_profissional()

        horario = { 
            'date': datetime.strptime('24/05/2050', '%d/%m/%Y'), 
            'startTime': '11:00', 
            'endTime': '11:45', 
            'livre': True, 
            'local_id': local.id, 
            'profissional_id': profissional.id, 
            'duracao': 45
        } 
        self.client.post(url_for('agenda.post_horario'), json=horario, headers=self.token)
        response = self.client.get(url_for('agenda.get_horario_profissional',
            selecao='especialidade',
            dt_inicio='23/05/2050',
            dt_fim = '24/05/2050',
            livre = 'true',
            especialdade_id = profissional.perfil_id), headers=self.token)
        # import ipdb; ipdb.set_trace()
        self.assertEqual(response.status_code, 200)

    def insere_uma_nova_consulta(self):
        self.client.post(url_for('profissional.profissional'), json=self.profissional_json, headers=self.token)
        profissional = Profissional.query.filter_by(cpf=self.profissional_json['cpf']).first()
        self.client.post(url_for('agenda.post_sala', descricao='sala teste'), headers=self.token)
        local = Local.query.filter_by(descricao='sala teste').first()

        horario = { 
            'date': datetime.strptime('24/05/2050', '%d/%m/%Y'), 
            'startTime': '11:00', 
            'endTime': '11:45', 
            'livre': True, 
            'local_id': local.id, 
            'profissional_id': profissional.id, 
            'duracao': 45
        } 
        self.client.post(url_for('agenda.post_horario'), json=horario, headers=self.token)
        h = Horario.query.filter_by(dt_dia = datetime.strptime('24/05/2050', '%d/%m/%Y')).first()

        # TODO: A estrutura de consulta mudou, devo consertar aqui e no front
        # TODO: Criar Profissional, Paciente, Horario, Salas, etc... no setup
        # TODO: Apagar no teardown
        consulta = { 
            'dataMarcacao': datetime.strptime('24/05/2050', '%d/%m/%Y'), 
            'confirmacao_consulta_sms': False, 
            'compareceu': False, 
            'paciente': { 
                'id': profissional.id, 
                'nome': profissional.nome 
            }, 
            'quem_marcou_id': profissional.id, 
            'horario_id': h.id, 
            'convenio': { 
                'id': self.ps_paciente.id, 
                'descricao': 'Teste'} 
        } 
        response = self.client.post(url_for('agenda.post_consulta'), json=consulta, headers=self.token)
        # import ipdb; ipdb.set_trace()
        self.assertEqual(response.status_code, 201)
        


        


