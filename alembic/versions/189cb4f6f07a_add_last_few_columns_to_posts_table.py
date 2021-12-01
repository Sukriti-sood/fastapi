"""add last few columns to posts table

Revision ID: 189cb4f6f07a
Revises: f14096a5c36e
Create Date: 2021-12-01 11:01:59.703445

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '189cb4f6f07a'
down_revision = 'f14096a5c36e'
branch_labels = None
depends_on = None


def upgrade():

    op.add_column('posts', sa.Column('published', sa.String(),
                  nullable=False, server_default='True'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                                     server_default=sa.text('now()'), nullable=False))
    pass


def downgrade():

    op.drop_column('posts', 'created_at')
    op.drop_column('posts', 'published')
    pass
