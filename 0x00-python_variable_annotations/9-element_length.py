#!/usr/bin/env python3
"""
This module contains a function that returns
a list of tuples with an element and its length.
"""

from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Function to return a list of tuples with an
    element and its length.

    Parameters:
    lst (Iterable[Sequence]): The iterable of sequences.

    Returns:
    List[Tuple[Sequence, int]]: The list of tuples with
    a sequence and its length.
    """

    return [(i, len(i)) for i in lst]
