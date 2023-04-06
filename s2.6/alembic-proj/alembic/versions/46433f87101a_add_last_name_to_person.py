"""add last_name to person

Revision ID: 46433f87101a
Revises: 5a0b3a6e66cd
Create Date: 2023-03-15 19:39:37.554419

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "46433f87101a"
down_revision = "5a0b3a6e66cd"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "person", sa.Column("last_name", sa.String(50), nullable=True)
    )


def downgrade() -> None:
    op.drop_column("person", "last_name")
