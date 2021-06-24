"""empty message

Revision ID: 984dc1192790
Revises: 3335d744ce14
Create Date: 2021-06-24 14:12:24.567654

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '984dc1192790'
down_revision = '3335d744ce14'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('HospitalDB',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('who', sa.String(), nullable=True),
    sa.Column('passphrase', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('cars')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cars',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('model', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('doors', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='cars_pkey')
    )
    op.drop_table('HospitalDB')
    # ### end Alembic commands ###