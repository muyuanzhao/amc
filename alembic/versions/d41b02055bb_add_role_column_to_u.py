"""add role column to user table

Revision ID: d41b02055bb
Revises: None
Create Date: 2013-02-25 19:02:22.252318

"""

# revision identifiers, used by Alembic.
revision = 'd41b02055bb'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('user', sa.Column('role', sa.String(64)))


def downgrade():
    op.drop_column('user', 'role')
