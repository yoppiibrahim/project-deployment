"""
This module provides functionalities to load dataframe a database.

It include a function to extract data fro the RentApartments table
in the database and load it into a panda DataFrame. This module is useful
analysis or processing. it uses SQLAlchemy for executing database queries
and pandas for handling the data in a DataFrame format.
"""

import pandas as pd
from loguru import logger
from sqlalchemy import select

from config import engine
from db.db_model import RentApartments


def load_data_from_db() -> pd.DataFrame:
    """
    Extract the entire RentApartments table from the database.

    Return:
        pd.DataFrame : DataFrame containing the RentApartments
    """
    logger.info("extracting the table from the database")
    query = select(RentApartments)
    return pd.read_sql(
        query,
        engine,
    )
