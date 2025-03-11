"""
This modul sets up the  ML model configuration.

It utilizes Pydantic's BaseSettings for configuration managements,
allowing settings to be read from environment variables and a .env file.

"""

from pydantic import DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict


class ModelSettings(BaseSettings):
    """
    Ml model Configuration settings  for the application.

    Attributes:
        model_config (SettingsConfigDict): model config load's from .env file.
        model_path (DirectoryPath): File system path to be model.
        log_level (str): Logging level for the application.
        model_name (str): Name of the ML model.
    """

    model_config = SettingsConfigDict(
        env_file="config/.env", env_model_encoding="utf-8", extra="ignore"
    )

    model_path: DirectoryPath
    model_name: str


model_settings = ModelSettings()
