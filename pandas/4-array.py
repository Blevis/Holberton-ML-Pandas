#!/usr/bin/env python3
"""
Module to extract the last 10 rows of High and Close columns as a numpy array.
"""
import pandas as pd


def array(df):
    """
    Selects the last 10 rows of the High and Close columns and converts
    them into a numpy.ndarray.

    Args:
        df (pandas.DataFrame): The input dataframe.

    Returns:
        numpy.ndarray: The resulting numpy array.
    """
    return df[['High', 'Close']].tail(10).to_numpy()
