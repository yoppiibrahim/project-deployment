import re

import pandas as pd
from loguru import logger

from model.pipeline.collection import load_data_from_db


def prepare_data() -> pd.DataFrame:
    """
    Prepare the dataset for analysis and modeling.

    This involves loading the dataframe, encoding categorical columns,
    and parsing the 'garden' column
    """
    logger.info("starting up preparation pipeline")
    dataframe = load_data_from_db()
    decode_data = _decode_cat_cols(dataframe)
    return _parse_garden_col(decode_data)


def _decode_cat_cols(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Encode categorical column into dummy variable.

    Arg:
        dataframe (pd.DataFrame): The original database.

    Return:
        pd.DataFrame: Database with categorical columns encoded.
    """
    cols = ["balcony", "parking", "furnished", "garage", "storage"]
    logger.info(f"encoding categorical colmn: {cols}")
    return pd.get_dummies(
        dataframe,
        columns=cols,
        dtype=int,
        drop_first=True,
    )


def _parse_garden_col(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Parse the 'garden' column in the dataset.

    Args:
        dataframe (pd.DataFrame): The dataset with a 'garden' column

    Returns:
        pd.DataFrame: The dataset with the 'garden' column parse.
    """
    logger.info("parsing garden column")
    dataframe['garden'] = dataframe['garden'].apply(
        lambda x: 0 if x == 'Not present' else int(re.findall(r'\d+', x)[0]),
    )
    return dataframe
