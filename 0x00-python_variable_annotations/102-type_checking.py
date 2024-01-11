#!/usr/bin/env python3
"""
This module contains a function that returns a list with each
element of the input list repeated a number of times.
"""

from typing import List, Tuple, Union


def zoom_array(lst: Tuple[Union[int,
               float]], factor: int = 2) -> List[Union[int, float]]:
    """
    Function to return a list with each element of the input
    list repeated a number of times.

    Parameters:
    lst (Tuple[Union[int, float]]): The tuple of integers and/or floats.
    factor (int): The number of times each element should be repeated.

    Returns:
    List[Union[int, float]]: The list with each element of the input
    list repeated a number of times.
    """

    zoomed_in: List[Union[int, float]] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
