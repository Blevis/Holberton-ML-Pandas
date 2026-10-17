#!/usr/bin/env python3
"""
Module to create a pandas.DataFrame from a numpy.ndarray.
"""
import pandas as pd


def from_numpy(array):
    """
    Creates a pd.DataFrame from a np.ndarray.

    Args:
        array (numpy.ndarray): The source array.

    Returns:
        pandas.DataFrame: The resulting dataframe with capitalized
                          alphabetical column labels.
    """
    cols = [chr(65 + i) for i in range(array.shape[1])]
    return pd.DataFrame(array, columns=cols)
