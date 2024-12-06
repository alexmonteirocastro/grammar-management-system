"""Create initial tables

Revision ID: d0c7619a3730
Revises: 
Create Date: 2024-12-05 21:43:50.351545+00:00

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd0c7619a3730'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('languages',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('code', sa.String(length=2), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_languages_code'), 'languages', ['code'], unique=True)
    op.create_index(op.f('ix_languages_id'), 'languages', ['id'], unique=False)
    op.create_index(op.f('ix_languages_name'), 'languages', ['name'], unique=True)
    op.create_table('cases',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('language_id', sa.UUID(), nullable=True),
    sa.Column('name_english', sa.String(), nullable=True),
    sa.Column('name_native', sa.String(), nullable=True),
    sa.Column('question', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['language_id'], ['languages.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_cases_id'), 'cases', ['id'], unique=False)
    op.create_index(op.f('ix_cases_name_english'), 'cases', ['name_english'], unique=False)
    op.create_index(op.f('ix_cases_name_native'), 'cases', ['name_native'], unique=False)
    op.create_table('word_patterns',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('language_id', sa.UUID(), nullable=True),
    sa.Column('base_word', sa.String(), nullable=True),
    sa.Column('type', sa.Enum('NOUN', 'ADJECRIVE', name='wordtype'), nullable=True),
    sa.Column('number', sa.Enum('SINGULAR', 'PLURAL', name='wordnumber'), nullable=True),
    sa.Column('gender', sa.Enum('MASCULINE', 'FEMININE', 'NEUTER', name='wordgender'), nullable=True),
    sa.ForeignKeyConstraint(['language_id'], ['languages.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_word_patterns_base_word'), 'word_patterns', ['base_word'], unique=False)
    op.create_index(op.f('ix_word_patterns_id'), 'word_patterns', ['id'], unique=False)
    op.create_table('word_forms',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('word_pattern_id', sa.UUID(), nullable=True),
    sa.Column('case_id', sa.UUID(), nullable=True),
    sa.Column('form', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['case_id'], ['cases.id'], ),
    sa.ForeignKeyConstraint(['word_pattern_id'], ['word_patterns.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_word_forms_id'), 'word_forms', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_word_forms_id'), table_name='word_forms')
    op.drop_table('word_forms')
    op.drop_index(op.f('ix_word_patterns_id'), table_name='word_patterns')
    op.drop_index(op.f('ix_word_patterns_base_word'), table_name='word_patterns')
    op.drop_table('word_patterns')
    op.drop_index(op.f('ix_cases_name_native'), table_name='cases')
    op.drop_index(op.f('ix_cases_name_english'), table_name='cases')
    op.drop_index(op.f('ix_cases_id'), table_name='cases')
    op.drop_table('cases')
    op.drop_index(op.f('ix_languages_name'), table_name='languages')
    op.drop_index(op.f('ix_languages_id'), table_name='languages')
    op.drop_index(op.f('ix_languages_code'), table_name='languages')
    op.drop_table('languages')
    # ### end Alembic commands ###
