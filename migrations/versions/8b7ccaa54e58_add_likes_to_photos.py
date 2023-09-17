"""add likes to photos

Revision ID: 8b7ccaa54e58
Revises: 9ac74b97ce4e
Create Date: 2023-09-17 17:55:40.227770

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b7ccaa54e58'
down_revision = '9ac74b97ce4e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('photo_likes',
    sa.Column('photo_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['photo_id'], ['photo.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('photo_likes')
    # ### end Alembic commands ###
