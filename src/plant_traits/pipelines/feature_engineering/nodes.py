"""
This is a boilerplate pipeline 'feature_engineering'
generated using Kedro 0.19.8
"""
# =================
# ==== IMPORTS ====
# =================
import pandas as pd

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
    df['file_path'] = df['id'].apply(lambda s: f'{path_images}/train_images/{s}.jpeg')
    return df
