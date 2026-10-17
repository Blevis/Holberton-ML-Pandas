#!/usr/bin/env python3
"""
Module to clean and fill missing values in a cryptocurrency dataframe.
"""


def fill(df):
    """
    Cleans and fills missing values in a pandas.DataFrame according to spec.

    Args:
        df (pandas.DataFrame): The input dataframe.

    Returns:
        pandas.DataFrame: The modified dataframe.
    """
    df = df.drop(columns=['Weighted_Price'])
    df['Close'] = df['Close'].ffill()
    df['High'] = df['High'].fillna(df['Close'])
    df['Low'] = df['Low'].fillna(df['Close'])
    df['Open'] = df['Open'].fillna(df['Close'])
    df['Volume_(BTC)'] = df['Volume_(BTC)'].fillna(0)
    df['Volume_(Currency)'] = df['Volume_(Currency)'].fillna(0)
    return df
