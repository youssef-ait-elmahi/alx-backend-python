#!/usr/bin/env python3
"""
This module contains a function that returns
the value of a key in a dictionary or a default value.
"""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None]) -> Union[Any, T]:
    """
    Function to return the value of a key in a
    dictionary or a default value.

    Parameters:
    dct (Mapping): The dictionary.
    key (Any): The key.
    default (Union[T, None]): The default value.

    Returns:
    Union[Any, T]: The value of the key in the dictionary or
    the default value.
    """

    if key in dct:
        return dct[key]
    else:
        return default
