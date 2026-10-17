#!/usr/bin/env python3
"""
Module to load data from a file into a pandas.DataFrame.
"""
import pandas as pd


def from_file(filename, delimiter):
    """
    Loads data from a file as a pandas.DataFrame.

    Args:
        filename (str): The path to the file to load from.
        delimiter (str): The column separator.

    Returns:
    pandas.DataFrame: The loaded dataframe.
    """
    return pd.read_csv(filename, sep=delimiter)
