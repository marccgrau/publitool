"""create account table

Revision ID: 860c68e3dff9
Revises: 
Create Date: 2023-04-04 18:14:53.197651

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '860c68e3dff9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("first_name", sa.String(length=256), nullable=True),
        sa.Column("surname", sa.String(length=256), nullable=True),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("is_superuser", sa.Boolean(), nullable=True),
        sa.Column("hashed_password", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_user_email"), "user", ["email"], unique=False)
    op.create_index(op.f("ix_user_id"), "user", ["id"], unique=False)
    op.create_table(
        "post",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("submitter_id", sa.Integer(), nullable=True),
        sa.Column("image", sa.String(length=256), nullable=True),
        sa.Column("text", sa.String(length=256), nullable=True),
        sa.ForeignKeyConstraint(
            ["submitter_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_post_id"), "post", ["id"], unique=False)



def downgrade() -> None:
    op.drop_index(op.f("ix_user_id"), table_name="user")
    op.drop_index(op.f("ix_user_email"), table_name="user")
    op.drop_table("user")
    op.drop_index(op.f("ix_post_id"), table_name="post")
    op.drop_table("post")
