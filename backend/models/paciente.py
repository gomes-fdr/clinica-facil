from . import db
import csv
from sqlalchemy.exc import SQLAlchemyError


class Paciente(db.Model):
    """
    Pacientes tratados na clinica
    """
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100))
    dt_nascimento = db.Column(db.DateTime)
    cpf = db.Column(db.String(11))
    rg = db.Column(db.String(10))
    filiacao = db.Column(db.String(100))
    profissao = db.Column(db.String(100))
    responsavel = db.Column(db.String(100))
    t_celular = db.Column(db.String(20))
    t_fixo = db.Column(db.String(20))
    t_responsavel = db.Column(db.String(20))
    cep = db.Column(db.String(15))
    rua = db.Column(db.String(100))
    numero = db.Column(db.String(30))
    complemento = db.Column(db.String(100))
    cidade = db.Column(db.String(100))
    estado = db.Column(db.String(100))
    observacoes = db.Column(db.String(100))
    envioSMS = db.Column(db.Boolean, default=False)
    adultoInapto = db.Column(db.Boolean, default=False)

    @staticmethod
    def import_pacientes(f_name):
        with open(f_name, mode='r') as f:
            fr = csv.DictReader(f)
            line=0
            for row in fr:
                if line == 0:
                    print(f'Colunas {", ".join(row)}')
                    line += 1
                # print(f'\t{row["nome"]}')
                p = Paciente(
                    nome = row["nome"],
                    email = row["email"],
                    dt_nascimento = row["datanasc"],
                    cpf = row["cpf"],
                    rg = row["rg"],
                    profissao = row["prodissao"],
                    responsavel = row["responsavel"],
                    t_celular = row["celular"],
                    t_fixo = row["telefone"],
                    cep = row["cep"],
                    rua = row["endereco"],
                    numero = row["numero"],
                    complemento = row["complemento"],
                    cidade = row["cidade"],
                    estado = row["estado"]
                )
                try:
                    db.session.add(p)
                    db.session.commit()
                except SQLAlchemyError as e:
                    # print(f'ERRO: {row["nome"]}')
                    print(e)
                line += 1
            print(f'Processado {line} linhas.')


# Versão com controle de campos nulos
# class Paciente(db.Model):
#     """
#     Pacientes tratados na clinica
#     """
#     id = db.Column(db.Integer, primary_key=True)
#     nome = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(100))
#     dt_nascimento = db.Column(db.DateTime, nullable=False)
#     cpf = db.Column(db.String(11), index=True, unique=True, nullable=False)
#     rg = db.Column(db.String(10))
#     filiacao = db.Column(db.String(100), nullable=False)
#     profissao = db.Column(db.String(100))
#     responsavel = db.Column(db.String(100))
#     t_celular = db.Column(db.String(20))
#     t_fixo = db.Column(db.String(20))
#     t_responsavel = db.Column(db.String(20))
#     cep = db.Column(db.String(15))
#     rua = db.Column(db.String(100), nullable=False)
#     numero = db.Column(db.String(10), nullable=False)
#     complemento = db.Column(db.String(100))
#     cidade = db.Column(db.String(100), nullable=False)
#     estado = db.Column(db.String(100), nullable=False)
#     envioSMS = db.Column(db.Boolean, default=False)
#     adultoInapto = db.Column(db.Boolean, default=False)

