#!/usr/bin/env python3
from typing import Mapping, Any, TypeVar, Union

T = TypeVar("T")


"""Returns the value for key in dct or default if not found"""


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """Returns the value for key in dct or default if not found."""
    if key in dct:
        return dct[key]
    else:
        return default
