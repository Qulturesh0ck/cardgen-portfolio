"""empty message

Revision ID: a4793bbf7c3c
Revises: 297a99546c72
Create Date: 2023-02-25 00:05:53.049200

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a4793bbf7c3c'
down_revision = '297a99546c72'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cards',
    sa.Column('card_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('description', sa.String(length=250), nullable=True),
    sa.Column('bp', sa.String(length=4), nullable=True),
    sa.Column('hp', sa.String(length=4), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('card_id')
    )
    op.create_table('generated_cards',
    sa.Column('gen_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('imagepath', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('card_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['card_id'], ['cards.card_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('gen_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('generated_cards')
    op.drop_table('cards')
    # ### end Alembic commands ###
