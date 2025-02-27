"""Add last_login column to user_account

Revision ID: 49083ae27ef0
Revises: a3afeda948e8
Create Date: 2024-12-08 20:09:29.675531

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '49083ae27ef0'
down_revision: Union[str, None] = 'a3afeda948e8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_account', sa.Column('last_login', sa.DateTime(timezone=True), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_account', 'last_login')
    # ### end Alembic commands ###
