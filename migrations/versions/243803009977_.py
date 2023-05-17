"""empty message

Revision ID: 243803009977
Revises: 00782764a548
Create Date: 2023-05-16 20:11:35.917409

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '243803009977'
down_revision = '00782764a548'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('planet_name', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('planet_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planet')
    # ### end Alembic commands ###
