"""empty message

Revision ID: 5494fc551177
Revises: 3f3fc59841d4
Create Date: 2019-04-04 11:07:46.426327

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5494fc551177'
down_revision = '3f3fc59841d4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('perfil',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('descricao', sa.String(length=100), nullable=True),
    sa.Column('permissao', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('situacao',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('descricao', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('profissional',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('dt_nascimento', sa.DateTime(), nullable=False),
    sa.Column('cpf', sa.String(length=11), nullable=False),
    sa.Column('rg', sa.String(length=10), nullable=True),
    sa.Column('faculdade', sa.String(length=100), nullable=False),
    sa.Column('no_conselho', sa.String(length=100), nullable=True),
    sa.Column('t_celular', sa.String(length=20), nullable=True),
    sa.Column('t_fixo', sa.String(length=20), nullable=True),
    sa.Column('cep', sa.String(length=15), nullable=True),
    sa.Column('rua', sa.String(length=100), nullable=False),
    sa.Column('numero', sa.String(length=10), nullable=False),
    sa.Column('complemento', sa.String(length=100), nullable=True),
    sa.Column('cidade', sa.String(length=100), nullable=False),
    sa.Column('estado', sa.String(length=100), nullable=False),
    sa.Column('perfil_id', sa.Integer(), nullable=True),
    sa.Column('situacao_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['perfil_id'], ['perfil.id'], ),
    sa.ForeignKeyConstraint(['situacao_id'], ['situacao.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('rg')
    )
    op.create_index(op.f('ix_profissional_cpf'), 'profissional', ['cpf'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_profissional_cpf'), table_name='profissional')
    op.drop_table('profissional')
    op.drop_table('situacao')
    op.drop_table('perfil')
    # ### end Alembic commands ###