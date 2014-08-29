"""add image_url to location

Revision ID: 208ed1ead94
Revises: 3bddda627f2a
Create Date: 2014-08-27 02:29:56.678884

"""

# revision identifiers, used by Alembic.
revision = '208ed1ead94'
down_revision = '3bddda627f2a'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('location', sa.Column('image_url', sa.String(length=256), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('location', 'image_url')
    ### end Alembic commands ###