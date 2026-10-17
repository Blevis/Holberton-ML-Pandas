#!/usr/bin/env python3
"""
Module to concatenate and rearrange MultiIndex DataFrames.
"""
import pandas as pd
index = __import__('10-index').index


def hierarchy(df1, df2):
    """
    Concatenates bitstamp and coinbase data for a specific timestamp range,
    rearranges the MultiIndex to have Timestamp first, and sorts chronologically.

    Args:
        df1 (pandas.DataFrame): Coinbase dataframe.
        df2 (pandas.DataFrame): Bitstamp dataframe.

    Returns:
        pandas.DataFrame: The transformed dataframe.
    """
    df1_indexed = index(df1)
    df2_indexed = index(df2)

    start_ts = 1417411980
    end_ts = 1417417980

    df1_sliced = df1_indexed.loc[start_ts:end_ts]
    df2_sliced = df2_indexed.loc[start_ts:end_ts]

    combined = pd.concat([df2_sliced, df1_sliced], keys=['bitstamp', 'coinbase'])

    return combined.swaplevel(0, 1).sort_index()
