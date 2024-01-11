#!/usr/bin/env python3
"""
This module contains a function that returns a list with each
element of the input list repeated a number of times.
"""

from typing import List, Tuple, Union


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
