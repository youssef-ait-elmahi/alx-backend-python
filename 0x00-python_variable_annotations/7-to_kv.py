#!/usr/bin/env python3
"""
This module contains a function that returns
a tuple with a string and the square of a number.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Function to return a tuple with a string and the
    quare of a number.

    Parameters:
    k (str): The string.
    v (Union[int, float]): The number.

    Returns:
    Tuple[str, float]: The tuple with the string and the
    square of the number.
    """

    return k, v**2
