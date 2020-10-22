#!/usr/bin/env python3
"""complex types functions"""
from typing import Callable, Iterator, Union, Optional, List


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    takes a float multiplier as argument
    """
    def ret(i: float) -> float:
        """
        take a float i as argument
        """
        return i * multiplier
    return ret
