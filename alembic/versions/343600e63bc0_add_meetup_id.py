"""add meetup_id

Revision ID: 343600e63bc0
Revises: a99b9eff4dc
Create Date: 2014-09-19 03:00:03.483052

"""

# revision identifiers, used by Alembic.
revision = '343600e63bc0'
down_revision = 'a99b9eff4dc'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('meetup_id', sa.String(length=255), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'meetup_id')
    ### end Alembic commands ###
