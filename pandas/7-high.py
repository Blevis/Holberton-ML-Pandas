#!/usr/bin/env python3
"""
Module to sort a dataframe by the High price in descending order.
"""


def high(df):
    """
    Sorts a DataFrame by the High column in descending order.

    Args:
        df (pandas.DataFrame): The input dataframe.

    Returns:
        pandas.DataFrame: The sorted dataframe.
    """
    return df.sort_values(by="High", ascending=False)
