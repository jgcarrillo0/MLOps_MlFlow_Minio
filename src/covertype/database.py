import os

from sqlalchemy import Engine, create_engine


def build_data_database_url() -> str:
    user = os.environ["DATA_DB_USER"]
    password = os.environ["DATA_DB_PASSWORD"]
    host = os.getenv("DATA_DB_HOST", "postgres-data")
    port = os.getenv("DATA_DB_PORT", "5432")
    database = os.environ["DATA_DB_NAME"]

    return f"postgresql+psycopg://{user}:{password}@{host}:{port}/{database}"


def get_data_engine() -> Engine:
    return create_engine(
        build_data_database_url(),
        pool_pre_ping=True,
    )
