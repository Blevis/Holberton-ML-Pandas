#!/usr/bin/env python3
"""
Module to rename a column, convert timestamps to datetimes,
and select specific columns in a pandas.DataFrame.
"""
import pandas as pd


def rename(df):
    """
    Renames Timestamp to Datetime, converts it to datetime,
    and returns a DataFrame with Datetime and Close columns.

    Args:
        df (pandas.DataFrame): The input dataframe.

    Returns:
        pandas.DataFrame: The modified dataframe.
    """
    df = df.rename(columns={"Timestamp": "Datetime"})
    df["Datetime"] = pd.to_datetime(df["Datetime"], unit="s")
    return df[["Datetime", "Close"]]
