"""empty message

Revision ID: 03cfabc8269f
Revises: c8eb7753b50a
Create Date: 2019-04-28 10:38:24.117169

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '03cfabc8269f'
down_revision = 'c8eb7753b50a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('horario', sa.Column('dt_dia', sa.DateTime(), nullable=True))
    op.add_column('horario', sa.Column('hora_fim', sa.String(length=5), nullable=True))
    op.add_column('horario', sa.Column('hora_ini', sa.String(length=5), nullable=True))
    op.drop_column('horario', 'dt_inicio')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('horario', sa.Column('dt_inicio', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_column('horario', 'hora_ini')
    op.drop_column('horario', 'hora_fim')
    op.drop_column('horario', 'dt_dia')
    # ### end Alembic commands ###
