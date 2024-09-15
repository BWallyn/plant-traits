"""
This is a boilerplate pipeline 'donwload_data'
generated using Kedro 0.19.8
"""
# =================
# ==== IMPORTS ====
# =================

# import kaggle
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi

# ===================
# ==== FUNCTIONS ====
# ===================

def download_data() -> pd.DataFrame:
    """
    """
    api = KaggleApi()
    api.authenticate()

