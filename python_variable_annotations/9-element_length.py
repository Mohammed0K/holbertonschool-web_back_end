#!/usr/bin/env python3
"""Returns a list of sequence in lst"""
from typing import Iterable, Sequence, List, Tuple


"""Returns afor each sequence in lst"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of  for each sequence in lst."""
    return [(i, len(i)) for i in lst]
