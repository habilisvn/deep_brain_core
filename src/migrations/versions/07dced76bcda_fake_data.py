"""fake data

Revision ID: 07dced76bcda
Revises: 55a13fafd082
Create Date: 2024-11-15 02:10:01.827566

"""
from typing import Sequence, Union
from datetime import datetime
from uuid import uuid4
import hashlib

from alembic import op
import sqlalchemy as sa
from faker import Faker


# revision identifiers, used by Alembic.
revision: str = '07dced76bcda'
down_revision: Union[str, None] = '55a13fafd082'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    fake = Faker()
    users = sa.table(
        'users',
        sa.column('id', sa.UUID),
        sa.column('email', sa.String),
        sa.column('username', sa.String),
        sa.column('password', sa.String),
        sa.column('is_active', sa.Boolean),
        sa.column('is_superuser', sa.Boolean),
        sa.column('created_at', sa.DateTime),
        sa.column('updated_at', sa.DateTime)
    )

    # Insert in batches of 1000 to avoid memory issues
    batch_size = 1000
    total_users = 10_000

    for i in range(0, total_users, batch_size):
        batch = [
            {
                'id': str(uuid4()),
                'email': f"{fake.user_name()}_{uuid4().hex[:12]}@gmail.com",
                'username': f"{fake.user_name()}_{uuid4().hex[:12]}",
                'password': (hashlib.sha512(fake.password().encode())
                             .hexdigest()),
                'is_active': True,
                'is_superuser': False,
                'created_at': datetime.now(),
                'updated_at': datetime.now()
            }
            for _ in range(min(batch_size, total_users - i))
        ]
        op.bulk_insert(users, batch)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute('TRUNCATE TABLE users')
    # ### end Alembic commands ###
