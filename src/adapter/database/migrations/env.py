import sys

sys.path.append('..')

from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

from src.adapter.database.config import db_config
from src.adapter.database.models.base import Base
from src.adapter.database.models.auth import User
from src.adapter.database.models.todo import Todo

config = context.config

section = config.config_ini_section

config.set_section_option(section, 'DB_HOST', db_config.DB_HOST)
config.set_section_option(section, 'DB_NAME', db_config.DB_NAME)
config.set_section_option(section, 'DB_PORT', db_config.DB_PORT)
config.set_section_option(section, 'DB_USER', db_config.DB_USER)
config.set_section_option(section, 'DB_PASSWORD', db_config.DB_PASSWORD)
config.set_section_option(section, 'DB_TYPE', db_config.DB_TYPE)
config.set_section_option(section, 'DB_CONNECTOR', db_config.DB_CONNECTOR)


if config.config_file_name is not None:
    fileConfig(config.config_file_name)


target_metadata = [Base.metadata]



def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
