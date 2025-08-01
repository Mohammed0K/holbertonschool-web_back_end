#!/usr/bin/env python3
"""Returns the first element of a sequence or None if the sequence is empty"""
from typing import Sequence, Any, Optional


"""Returns the first element of a sequence or None if the sequence is empty"""


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Returns the first element of a sequence or None."""
    if lst:
        return lst[0]
    else:
        return None
