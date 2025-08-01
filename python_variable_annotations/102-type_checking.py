#!/usr/bin/env python3
"""Returns a list with each item repeated factor times"""
from typing import Tuple, List, Any


"""Returns a list with each item repeated factor times"""


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Returns a list with each item repeated factor times."""
    zoomed_in: List[Any] = [item for item in lst for i in range(factor)]
    return zoomed_in
