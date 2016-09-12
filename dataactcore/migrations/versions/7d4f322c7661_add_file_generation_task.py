"""add_file_generation_task

Revision ID: 7d4f322c7661
Revises: 31876fecc214
Create Date: 2016-09-02 12:08:21.113516

"""

# revision identifiers, used by Alembic.
revision = '7d4f322c7661'
down_revision = '31876fecc214'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_data_broker():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('file_generation_task',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('file_generation_task_id', sa.Integer(), nullable=False),
    sa.Column('generation_task_key', sa.Text(), nullable=True),
    sa.Column('submission_id', sa.Integer(), nullable=True),
    sa.Column('file_type_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['file_type_id'], ['file_type.file_type_id'], name='fk_generation_file_type'),
    sa.ForeignKeyConstraint(['submission_id'], ['submission.submission_id'], name='fk_generation_submission'),
    sa.PrimaryKeyConstraint('file_generation_task_id')
    )
    op.create_index(op.f('ix_file_generation_task_generation_task_key'), 'file_generation_task', ['generation_task_key'], unique=True)
    op.drop_table('d_file_metadata')
     ### end Alembic commands ###


def downgrade_data_broker():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('d_file_metadata',
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('d_file_id', sa.INTEGER(), nullable=False),
    sa.Column('type', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('submission_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('start_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('end_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('status_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('error_message', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('original_file_name', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('upload_file_name', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('is_submitted', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['status_id'], ['job_status.job_status_id'], name='fk_status_id'),
    sa.ForeignKeyConstraint(['submission_id'], ['submission.submission_id'], name='fk_submission_id'),
    sa.PrimaryKeyConstraint('d_file_id', name='d_file_metadata_pkey'),
    sa.UniqueConstraint('submission_id', 'type', name='_submission_type_uc')
    )
    op.drop_index(op.f('ix_file_generation_task_generation_task_key'), table_name='file_generation_task')
    op.drop_table('file_generation_task')
    ### end Alembic commands ###
