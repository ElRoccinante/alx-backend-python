#!/usr/bin/env python3
"""v.annotations"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """A function that we must add the variable annotation to."""
    if lst:
        return lst[0]
    else:
        return None
