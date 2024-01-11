#!/usr/bin/env python3
"""
This module contains a function that returns
a function that multiplies a float by a multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function to return a function that multiplies a
    float by a multiplier.

    Parameters:
    multiplier (float): The multiplier.

    Returns:
    Callable[[float], float]: The function that multiplies a
    float by the multiplier.
    """

    def multiplier_func(n: float) -> float:
        return n * multiplier

    return multiplier_func
