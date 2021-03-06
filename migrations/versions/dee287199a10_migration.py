""" migration

Revision ID: dee287199a10
Revises: 790c7e72ce7e
Create Date: 2018-10-14 16:13:42.480963

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dee287199a10'
down_revision = '790c7e72ce7e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('pitch', sa.String(length=1000), nullable=True))
    op.drop_column('pitches', 'body')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('body', sa.VARCHAR(length=300), autoincrement=False, nullable=True))
    op.drop_column('pitches', 'pitch')
    # ### end Alembic commands ###
