"""empty message

Revision ID: 5266c76b1957
Revises: 81a42c2f7712
Create Date: 2019-04-24 12:06:58.209948

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5266c76b1957'
down_revision = '81a42c2f7712'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('idx_ps_paciente', table_name='plano_saude_paciente')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('idx_ps_paciente', 'plano_saude_paciente', ['paciente_id', 'ps_id'], unique=False)
    # ### end Alembic commands ###
