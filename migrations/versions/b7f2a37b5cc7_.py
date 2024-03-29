"""empty message

Revision ID: b7f2a37b5cc7
Revises: 5b6468b682fc
Create Date: 2019-05-29 10:30:17.946726

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b7f2a37b5cc7'
down_revision = '5b6468b682fc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('consulta', 'p_id_quem_marcou',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('consulta', 'p_id_quem_marcou',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
