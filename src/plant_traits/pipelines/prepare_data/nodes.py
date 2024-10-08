"""
This is a boilerplate pipeline 'prepare_data'
generated using Kedro 0.19.8
"""
# =================
# ==== IMPORTS ====
# =================

import pandas as pd
from sklearn.model_selection import train_test_split
from tqdm.notebook import tqdm

# Options
tqdm.pandas()

# ===================
# ==== FUNCTIONS ====
# ===================

def add_path_to_images(df: pd.DataFrame, path_images: str) -> pd.DataFrame:
    """Add path to each image in the dataframe

    Args:
        df (pd.DataFrame): Input dataframe
        path_images (str): Path to the folder containing images
    Returns:
        df (pd.DataFrame): Output dataframe with path to images
    """
    df['file_path'] = df['id'].apply(lambda s: f'{path_images}/{s}.jpeg')
    return df


def add_jpeg_bytes(df: pd.DataFrame) -> pd.DataFrame:
    """Add the image as a bytes in a new column named jpeg_bytes

    Args:
        df (pd.DataFrame): Input dataframe
    Returns:
        df (pd.DataFrame): Output dataframe with the new column
    """
    df['jpeg_bytes'] = df['file_path'].progress_apply(lambda fp: open(fp, 'rb').read())
    return df


def split_train_test(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Split the dataset into train and test

    Args:
        df (pd.DataFrame): Input dataframe
    Returns:
        df_train (pd.DataFrame): Training dataframe
        df_test (pd.DataFrame): Test dataframe
    """
    df_train, df_test = train_test_split(df, test_size=0.2, shuffle=True, random_state=12)
    return df_train, df_test
