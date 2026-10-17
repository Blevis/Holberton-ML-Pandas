#!/usr/bin/env python3
"""
Module to compute descriptive statistics for a pandas DataFrame.
"""


def analyze(df):
    """
    Computes descriptive statistics for all
    columns except the Timestamp column.

    Args:
        df (pandas.DataFrame): The input dataframe.

    Returns:
        pandas.DataFrame: The descriptive statistics dataframe.
    """
    return df.drop(columns=['Timestamp']).describe()
