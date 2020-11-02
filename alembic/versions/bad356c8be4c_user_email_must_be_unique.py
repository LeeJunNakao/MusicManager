"""user email must be unique

Revision ID: bad356c8be4c
Revises: 80acd462cca4
Create Date: 2020-10-28 02:31:54.543687

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "bad356c8be4c"
down_revision = "80acd462cca4"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, "users", ["email"])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "users", type_="unique")
    # ### end Alembic commands ###
