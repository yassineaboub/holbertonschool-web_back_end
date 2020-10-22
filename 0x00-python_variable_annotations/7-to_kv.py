#!/usr/bin/env python3
"""string int float to tuple function"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    takes a string k and an int
    OR float v as arguments
    """
    return (k, v**2)
