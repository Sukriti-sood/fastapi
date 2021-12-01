"""add content colummn to post table

Revision ID: 0fbe3541338f
Revises: f334b59baf1b
Create Date: 2021-12-01 10:15:27.037192

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0fbe3541338f'
down_revision = 'f334b59baf1b'
branch_labels = None
depends_on = None


def upgrade():

    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
