#!/usr/bin/env python3
from typing import List, Union


"""Returns the sum of a list of ints and floats"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of a list of ints and floats as a float."""
    return float(sum(mxd_lst))
