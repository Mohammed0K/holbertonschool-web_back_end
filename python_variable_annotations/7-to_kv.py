#!/usr/bin/env python3
"""Returns a tuple with a string and the square of an int or float"""
from typing import Union, Tuple


"""Returns a tuple with a string and the square of an int or float"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple with a string and the square of an int or float."""
    return (k, float(v**2))
