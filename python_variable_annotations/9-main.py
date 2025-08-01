#!/usr/bin/env python3
"""This module provides a iterable."""

from typing import Iterable, Sequence, List, Tuple

def element_length(
    lst: Iterable[Sequence],
) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples 
    for each sequence in lst.
    """
    return [(i, len(i)) for i in lst]
