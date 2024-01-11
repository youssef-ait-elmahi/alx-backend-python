#!/usr/bin/env python3
"""
This module contains a function that returns a list with each
element of the input list repeated a number of times.
"""

from typing import List


def zoom_array(lst: List[int], factor: int = 2) -> List[int]:
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]

    return zoomed_in
