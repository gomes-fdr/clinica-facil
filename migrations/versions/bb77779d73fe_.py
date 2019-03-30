"""empty message

Revision ID: bb77779d73fe
Revises: 514f5b040d9c
Create Date: 2019-03-30 11:57:45.994375

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb77779d73fe'
down_revision = '514f5b040d9c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('paciente',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('dt_nascimento', sa.DateTime(), nullable=True),
    sa.Column('cpf', sa.String(length=11), nullable=True),
    sa.Column('rg', sa.String(length=10), nullable=True),
    sa.Column('filiacao', sa.String(length=100), nullable=True),
    sa.Column('profissao', sa.String(length=100), nullable=True),
    sa.Column('responsavel', sa.String(length=100), nullable=True),
    sa.Column('t_celular', sa.String(length=20), nullable=True),
    sa.Column('t_fixo', sa.String(length=20), nullable=True),
    sa.Column('t_responsavel', sa.String(length=20), nullable=True),
    sa.Column('cep', sa.String(length=15), nullable=True),
    sa.Column('rua', sa.String(length=100), nullable=True),
    sa.Column('numero', sa.String(length=10), nullable=True),
    sa.Column('complemento', sa.String(length=100), nullable=True),
    sa.Column('cidade', sa.String(length=100), nullable=True),
    sa.Column('estado', sa.String(length=100), nullable=True),
    sa.Column('envioSMS', sa.Boolean(), nullable=True),
    sa.Column('adultoInapto', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_paciente_cpf'), 'paciente', ['cpf'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_paciente_cpf'), table_name='paciente')
    op.drop_table('paciente')
    # ### end Alembic commands ###