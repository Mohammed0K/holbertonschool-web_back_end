#!/usr/bin/env python3

from typing import Iterable, Sequence, List, Tuple


# Returns a list of tuples (item, length of item) for each sequence in lst
def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples (item, length of item) for each sequence in lst."""
    return [(i, len(i)) for i in lst]
