#!/usr/bin/env python3
"""
Module to sort a dataframe in reverse chronological order and transpose it.
"""


def flip_switch(df):
    """
    Sorts data in reverse chronological order and transposes the dataframe.

    Args:
        df (pandas.DataFrame): The input dataframe.

    Returns:
        pandas.DataFrame: The transformed dataframe.
    """
    return df.sort_index(ascending=False).T
