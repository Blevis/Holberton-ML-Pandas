#!/usr/bin/env python3
"""
Module to set the index of a pandas.DataFrame to the Timestamp column.
"""


def index(df):
    """
    Sets the Timestamp column as the index of the dataframe.

    Args:
        df (pandas.DataFrame): The input dataframe.

    Returns:
        pandas.DataFrame: The modified dataframe with Timestamp as the index.
    """
    return df.set_index('Timestamp')
