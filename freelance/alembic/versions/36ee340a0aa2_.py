"""empty message

Revision ID: 36ee340a0aa2
Revises: 
Create Date: 2022-09-22 04:53:12.521441

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "36ee340a0aa2"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index("ix_gig_id", table_name="gig")
    op.drop_table("gig")
    op.drop_index("ix_request_id", table_name="request")
    op.drop_table("request")
    op.drop_index("ix_premiumpackage_id", table_name="premiumpackage")
    op.drop_table("premiumpackage")
    op.drop_index("ix_users_id", table_name="users")
    op.drop_table("users")
    op.drop_index("ix_gigimage_id", table_name="gigimage")
    op.drop_table("gigimage")
    op.drop_index("ix_gigvideo_id", table_name="gigvideo")
    op.drop_table("gigvideo")
    op.drop_index("ix_profileimg_id", table_name="profileimg")
    op.drop_table("profileimg")
    op.drop_index("ix_standardpackage_id", table_name="standardpackage")
    op.drop_table("standardpackage")
    op.drop_index("ix_profile_id", table_name="profile")
    op.drop_table("profile")
    op.drop_index("ix_basicpackage_id", table_name="basicpackage")
    op.drop_table("basicpackage")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "basicpackage",
        sa.Column("id", sa.INTEGER(), nullable=False),
        sa.Column("title", sa.VARCHAR(), nullable=False),
        sa.Column("basic_description", sa.VARCHAR(), nullable=False),
        sa.Column("delivery_date", sa.VARCHAR(), nullable=False),
        sa.Column("price", sa.INTEGER(), nullable=False),
        sa.Column("profile_id", sa.INTEGER(), nullable=True),
        sa.ForeignKeyConstraint(
            ["profile_id"],
            ["profile.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_basicpackage_id", "basicpackage", ["id"], unique=False)
    op.create_table(
        "profile",
        sa.Column("id", sa.INTEGER(), nullable=False),
        sa.Column("surname", sa.VARCHAR(), nullable=False),
        sa.Column("firstName", sa.VARCHAR(), nullable=False),
        sa.Column("lastName", sa.VARCHAR(), nullable=True),
        sa.Column("phone_no", sa.VARCHAR(), nullable=False),
        sa.Column("profileDescription", sa.VARCHAR(), nullable=False),
        sa.Column("school", sa.VARCHAR(), nullable=False),
        sa.Column("courseStudy", sa.VARCHAR(), nullable=False),
        sa.Column("certificate", sa.VARCHAR(), nullable=False),
        sa.Column("certifiedBy", sa.VARCHAR(), nullable=False),
        sa.Column("websiteUrl", sa.VARCHAR(), nullable=False),
        sa.Column("statusM", sa.VARCHAR(), nullable=False),
        sa.Column("user_id", sa.INTEGER(), nullable=True),
        sa.Column("request_id", sa.INTEGER(), nullable=True),
        sa.ForeignKeyConstraint(
            ["request_id"],
            ["request.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_profile_id", "profile", ["id"], unique=False)
    op.create_table(
        "standardpackage",
        sa.Column("id", sa.INTEGER(), nullable=False),
        sa.Column("title", sa.VARCHAR(), nullable=False),
        sa.Column("standard_description", sa.VARCHAR(), nullable=False),
        sa.Column("delivery_date", sa.VARCHAR(), nullable=False),
        sa.Column("price", sa.INTEGER(), nullable=False),
        sa.Column("profile_id", sa.INTEGER(), nullable=True),
        sa.ForeignKeyConstraint(
            ["profile_id"],
            ["profile.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_standardpackage_id", "standardpackage", ["id"], unique=False)
    op.create_table(
        "profileimg",
        sa.Column("id", sa.INTEGER(), nullable=False),
        sa.Column("picture", sa.VARCHAR(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_profileimg_id", "profileimg", ["id"], unique=False)
    op.create_table(
        "gigvideo",
        sa.Column("id", sa.INTEGER(), nullable=False),
        sa.Column("gig_video", sa.VARCHAR(), nullable=True),
        sa.Column("video_name", sa.VARCHAR(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_gigvideo_id", "gigvideo", ["id"], unique=False)
    op.create_table(
        "gigimage",
        sa.Column("id", sa.INTEGER(), nullable=False),
        sa.Column("picture_one", sa.VARCHAR(), nullable=True),
        sa.Column("contentby", sa.VARCHAR(), nullable=True),
        sa.Column("picture_two", sa.VARCHAR(), nullable=True),
        sa.Column("file_name_two", sa.VARCHAR(), nullable=True),
        sa.Column("video_file", sa.VARCHAR(), nullable=True),
        sa.Column("video_name", sa.VARCHAR(), nullable=True),
        sa.Column("file_doc", sa.VARCHAR(), nullable=True),
        sa.Column("content_type", sa.VARCHAR(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_gigimage_id", "gigimage", ["id"], unique=False)
    op.create_table(
        "users",
        sa.Column("id", sa.INTEGER(), nullable=False),
        sa.Column("username", sa.VARCHAR(), nullable=True),
        sa.Column("email", sa.VARCHAR(), nullable=False),
        sa.Column("password", sa.VARCHAR(), nullable=False),
        sa.Column("created_at", sa.DATE(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
        sa.UniqueConstraint("username"),
    )
    op.create_index("ix_users_id", "users", ["id"], unique=False)
    op.create_table(
        "premiumpackage",
        sa.Column("id", sa.INTEGER(), nullable=False),
        sa.Column("title", sa.VARCHAR(), nullable=False),
        sa.Column("premium_description", sa.VARCHAR(), nullable=False),
        sa.Column("delivery_date", sa.VARCHAR(), nullable=False),
        sa.Column("price", sa.INTEGER(), nullable=False),
        sa.Column("profile_id", sa.INTEGER(), nullable=True),
        sa.ForeignKeyConstraint(
            ["profile_id"],
            ["profile.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_premiumpackage_id", "premiumpackage", ["id"], unique=False)
    op.create_table(
        "request",
        sa.Column("id", sa.INTEGER(), nullable=False),
        sa.Column("description", sa.VARCHAR(length=150), nullable=True),
        sa.Column("price", sa.INTEGER(), nullable=True),
        sa.Column("dilivery_date", sa.VARCHAR(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_request_id", "request", ["id"], unique=False)
    op.create_table(
        "gig",
        sa.Column("id", sa.INTEGER(), nullable=False),
        sa.Column("title", sa.VARCHAR(length=88), nullable=False),
        sa.Column("search_tags", sa.VARCHAR(length=40), nullable=False),
        sa.Column("gig_description", sa.VARCHAR(length=800), nullable=False),
        sa.Column("gig_requirements", sa.VARCHAR(length=40), nullable=False),
        sa.Column("faq", sa.VARCHAR(), nullable=True),
        sa.Column("created_at", sa.VARCHAR(), nullable=True),
        sa.Column("is_active", sa.BOOLEAN(), nullable=True),
        sa.Column("users_id", sa.INTEGER(), nullable=True),
        sa.Column("profile_id", sa.INTEGER(), nullable=True),
        sa.Column("request_id", sa.INTEGER(), nullable=True),
        sa.Column("basic_package", sa.INTEGER(), nullable=True),
        sa.Column("standard_package", sa.INTEGER(), nullable=True),
        sa.Column("premium_package", sa.INTEGER(), nullable=True),
        sa.Column("gig_doc", sa.VARCHAR(), nullable=True),
        sa.Column("gig_video", sa.VARCHAR(), nullable=True),
        sa.Column("gig_image", sa.VARCHAR(), nullable=True),
        sa.ForeignKeyConstraint(
            ["basic_package"],
            ["basicpackage.id"],
        ),
        sa.ForeignKeyConstraint(
            ["premium_package"],
            ["premiumpackage.id"],
        ),
        sa.ForeignKeyConstraint(
            ["profile_id"],
            ["profile.id"],
        ),
        sa.ForeignKeyConstraint(
            ["request_id"],
            ["request.id"],
        ),
        sa.ForeignKeyConstraint(
            ["standard_package"],
            ["standardpackage.id"],
        ),
        sa.ForeignKeyConstraint(
            ["users_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_gig_id", "gig", ["id"], unique=False)
    # ### end Alembic commands ###
