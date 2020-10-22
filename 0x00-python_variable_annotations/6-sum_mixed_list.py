#!/usr/bin/env python3
"""mixed list function"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    takes a list mxd_lst of integers and floats
    """
    return sum(mxd_lst)
