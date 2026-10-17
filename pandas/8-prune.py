#!/usr/bin/env python3
"""
Module to remove rows with NaN values in the Close column.
"""


def prune(df):
    """
    Removes any entries where Close has NaN values.

    Args:
        df (pandas.DataFrame): The input dataframe.

    Returns:
        pandas.DataFrame: The modified dataframe.
    """
    return df.dropna(subset=['Close'])
