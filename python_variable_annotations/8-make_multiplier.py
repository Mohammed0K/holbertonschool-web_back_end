#!/usr/bin/env python3
from typing import Callable


# Returns a function that multiplies a float by multiplier
def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier."""
    return lambda x: x * multiplier
