#!/usr/bin/env python3
"""This module provides a function to return the length of elements in an iterable."""

from typing import Iterable, Sequence, List, Tuple


def element_length(
    lst: Iterable[Sequence],
) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples (item, length of item) for each sequence in lst."""
    return [(i, len(i)) for i in lst]
