#!/usr/bin/env python3
"""first element of a sequence"""
from typing import Callable, Iterator, Union, Optional, List, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Duck typing
    """
    if lst:
        return lst[0]
    else:
        return None
