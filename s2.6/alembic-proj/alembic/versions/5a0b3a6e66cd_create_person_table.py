"""create person table

Revision ID: 5a0b3a6e66cd
Revises: 
Create Date: 2023-03-15 19:35:17.865619

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "5a0b3a6e66cd"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "person",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(50), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("person")
