#!/usr/bin/python3
""" simple_helper_function """

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """summary"""
    return (((page - 1) * page_size), (page * page_size))
