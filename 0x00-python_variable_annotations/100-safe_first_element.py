#!/usr/bin/env python3
"""
This module contains a function that returns
the first element of a list or None.
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Function to return the first element of a list or None.

    Parameters:
    lst (Sequence[Any]): The list.

    Returns:
    Union[Any, None]: The first element of the list or None.
    """

    if lst:
        return lst[0]
    else:
        return None
