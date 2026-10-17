#!/usr/bin/env python3
"""
Module to concatenate two DataFrames with indexation and hierarchical keys.
"""
import pandas as pd
index = __import__('10-index').index


def concat(df1, df2):
    """
    Concatenates bitstamp data up to timestamp
    1417411920 to the top of coinbase data.

    Args:
        df1 (pandas.DataFrame): Coinbase dataframe.
        df2 (pandas.DataFrame): Bitstamp dataframe.

    Returns:
        pandas.DataFrame: The concatenated dataframe.
    """
    df1_indexed = index(df1)
    df2_indexed = index(df2)

    df2_sliced = df2_indexed.loc[:1417411920]

    return pd.concat([df2_sliced, df1_indexed], keys=['bitstamp', 'coinbase'])
