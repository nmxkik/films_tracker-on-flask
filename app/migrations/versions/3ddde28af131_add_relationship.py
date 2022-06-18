"""add relationship

Revision ID: 3ddde28af131
Revises: 7e2f33680d48
Create Date: 2022-06-17 19:34:25.387761

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '3ddde28af131'
down_revision = '7e2f33680d48'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('slug', table_name='post')
    op.drop_table('post')
    op.drop_table('tag')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tag',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(collation='utf8_unicode_ci', length=100), nullable=True),
    sa.Column('slug', mysql.VARCHAR(collation='utf8_unicode_ci', length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8_unicode_ci',
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB'
    )
    op.create_table('post',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', mysql.VARCHAR(collation='utf8_unicode_ci', length=140), nullable=True),
    sa.Column('cardtitle', mysql.VARCHAR(collation='utf8_unicode_ci', length=140), nullable=True),
    sa.Column('img', mysql.VARCHAR(collation='utf8_unicode_ci', length=280), nullable=True),
    sa.Column('slug', mysql.VARCHAR(collation='utf8_unicode_ci', length=140), nullable=True),
    sa.Column('country', mysql.VARCHAR(collation='utf8_unicode_ci', length=140), nullable=True),
    sa.Column('release_date', mysql.VARCHAR(collation='utf8_unicode_ci', length=140), nullable=True),
    sa.Column('genre', mysql.VARCHAR(collation='utf8_unicode_ci', length=140), nullable=True),
    sa.Column('cast_actors', mysql.VARCHAR(collation='utf8_unicode_ci', length=140), nullable=True),
    sa.Column('rating', mysql.FLOAT(), nullable=False),
    sa.Column('description', mysql.TEXT(collation='utf8_unicode_ci'), nullable=True),
    sa.Column('created', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id', 'rating'),
    mysql_collate='utf8_unicode_ci',
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB'
    )
    op.create_index('slug', 'post', ['slug'], unique=False)
    # ### end Alembic commands ###
