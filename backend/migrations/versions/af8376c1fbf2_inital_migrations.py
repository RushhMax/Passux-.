"""INital migrations

Revision ID: af8376c1fbf2
Revises: 
Create Date: 2024-07-28 11:26:06.807901

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af8376c1fbf2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('MESSAGES',
    sa.Column('message_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('sender_id', sa.Integer(), nullable=False),
    sa.Column('receiver_id', sa.Integer(), nullable=False),
    sa.Column('is_read', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['receiver_id'], ['USERS.user_id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['sender_id'], ['USERS.user_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('message_id')
    )
    op.create_table('POSTS',
    sa.Column('post_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['USERS.user_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('post_id')
    )
    op.create_table('COMMENTS',
    sa.Column('comment_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['POSTS.post_id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['USERS.user_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('comment_id')
    )
    op.create_table('REACTIONS',
    sa.Column('reaction_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('comment_id', sa.Integer(), nullable=True),
    sa.Column('type', sa.Enum('like', 'dislike', 'love', 'haha', 'wow', 'sad', 'angry', name='reaction_type'), nullable=True),
    sa.ForeignKeyConstraint(['comment_id'], ['COMMENTS.comment_id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['post_id'], ['POSTS.post_id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['USERS.user_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('reaction_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('REACTIONS')
    op.drop_table('COMMENTS')
    op.drop_table('POSTS')
    op.drop_table('MESSAGES')
    # ### end Alembic commands ###