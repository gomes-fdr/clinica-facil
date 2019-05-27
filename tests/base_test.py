from unittest import TestCase
from datetime import datetime
from flask import url_for, current_app
from json import loads
from backend import create_app

from backend.models.ps import PlanoSaude, PlanoSaudePaciente
from backend.models.paciente import Paciente
from backend.models.profissional import (Profissional, Situacao, Perfil, User)
from backend.models.agenda import Local, Horario

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
        self.ps = PlanoSaude.query.filter_by(descricao='Teste').first()
        self.situacao = Situacao.query.filter_by(descricao = 'Ativo').first()
        self.perfil = Perfil.query.filter_by(descricao = 'Psicologo').first()
        self.paciente_json = {
            'nome': 'paciente de testes',
            'email': 'teste@teste.com.br',
            'dt_nascimento': str(datetime.strptime('24/05/1974', '%d/%m/%Y')),
            'cpf': '01234567890',
            'rg': '0000000000',
            'filiacao': 'meu pai',
            'profissao': 'minha profissão',
            'responsavel': 'minha mãe',
            't_celular': '51999999999',
            't_fixo': '5133366903',
            't_responsavel': '51999999999',
            'cep': '99999000',
            'rua': 'Das Couves',
            'numero': '100',
            'complemento': 'casa',
            'cidade': 'Porto Alegre',
            'estado': 'RS',
            'observacoes': 'não tenho observações',
            'envioSMS': True,
            'adultoInapto': True,
            'situacao_id': self.situacao.id
        }
        self.paciente_alterado = {
            'nome': 'paciente de testes alterado',
            'email': 'teste@teste.com.br',
            'dt_nascimento': str(datetime.strptime('24/05/1984', '%d/%m/%Y')),
            'cpf': '01234567890',
            'rg': '0000000000',
            'filiacao': 'meu pai',
            'profissao': 'minha profissão',
            'responsavel': 'minha mãe',
            't_celular': '51999999999',
            't_fixo': '5133366903',
            't_responsavel': '51999999999',
            'cep': '99999000',
            'rua': 'Das Couves',
            'numero': '111',
            'complemento': 'casa',
            'cidade': 'Porto Alegre',
            'estado': 'RS',
            'observacoes': 'não tenho observações',
            'envioSMS': False,
            'adultoInapto': False,
            'situacao_id': self.situacao.id
        }
        self.paciente = Paciente.query.filter_by(cpf='01234567890').first()
        self.profissional_json = {
            'nome': 'Profissional de testes',
            'email': 'teste@teste.com.br',
            'dt_nascimento': str(datetime.strptime('24/05/1984', '%d/%m/%Y')),
            'cpf': '01234567890',
            'rg': '0000000000',
            'faculdade': 'NA',
            'no_conselho': '000',
            't_celular': '51999999999',
            't_fixo': '5133366903',
            'cep': '99999000',
            'rua': 'Das Couves',
            'numero': '111',
            'complemento': 'casa',
            'cidade': 'Porto Alegre',
            'estado': 'RS',
            'perfis': self.perfil.id,
            'situacoes': self.situacao.id
        }
        self.profissional_alterado = {
            'nome': 'Profissional de testes alterado',
            'email': 'teste@teste.com.br',
            'dt_nascimento': str(datetime.strptime('24/05/1994', '%d/%m/%Y')),
            'cpf': '01234567890',
            'rg': '0000000000',
            'faculdade': 'da vida',
            'no_conselho': '000',
            't_celular': '51999999999',
            't_fixo': '5133366903',
            'cep': '99999000',
            'rua': 'Das Couves',
            'numero': '111',
            'complemento': 'casa',
            'cidade': 'Porto Alegre',
            'estado': 'RS',
            'perfis': self.perfil.id,
            'situacoes': self.situacao.id
        }


    def tearDown(self):
        """
        Roda depois de todos os testes
        """
        # Apaga horario de testes
        Horario.query.filter_by(dt_dia = datetime.strptime('24/05/2050', '%d/%m/%Y')).delete()

        # Apaga plano de saude de paciente
        PlanoSaudePaciente.query.filter_by(no_carteira='teste-carteira').delete()

        # Apaga plano de saude testes
        PlanoSaude.query.filter_by(descricao='Teste').delete()

        # Apaga paciente de testes
        Paciente.query.filter_by(cpf=self.profissional_json['cpf']).delete()

        # Apaga profissional de testes
        Profissional.query.filter_by(cpf=self.profissional_json['cpf']).delete()

        # Apaga user de testes do banco de dados
        User.query.filter_by(email=self.paciente_json['email']).delete()

        # Apaga Local de atendimento de testes
        Local.query.filter_by(descricao = 'sala teste').delete()

        current_app.db.session.commit()

    def create_token(self):
        login = self.client.post(url_for('token.token'), json=self.user)
        return {
            'Authorization':
                'Bearer ' + loads(login.data.decode())['token']
}
