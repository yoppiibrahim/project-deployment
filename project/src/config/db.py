"""
This modul sets up database configuration.

It utilizes Pydantic's bassetting for configuration managements,
allowing settings to be read from environment variables and a .env file.

"""

from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import create_engine


class DbSettings(BaseSettings):
    """
    Configuration settings  for the application.

    Attributes:
        model_config (SettingsConfigDict): model config loads from .env file.
        log_level (str): Logging level for the application.
    """

    model_config = SettingsConfigDict(
        env_file="config/.env", env_model_encoding="utf-8", extra="ignore"
    )

    db_conn_str: str
    rent_apart_table_name: str


db_settings = DbSettings()

engine = create_engine(db_settings.db_conn_str)
