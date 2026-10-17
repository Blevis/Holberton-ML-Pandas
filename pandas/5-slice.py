#!/usr/bin/env python3
"""
Module to slice specific columns and every 60th row from a pandas.DataFrame.
"""


def slice(df):
    """
    Extracts High, Low, Close, and Volume_(BTC) columns and selects
    every 60th row.

    Args:
        df (pandas.DataFrame): The input dataframe.

    Returns:
        pandas.DataFrame: The sliced dataframe.
    """
    return df[['High', 'Low', 'Close', 'Volume_(BTC)']].iloc[::60]
