#!/usr/bin/env python3
"""complex types functions"""


from typing import Callable, Iterator, Union, Optional, List

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def ret(i:float) -> float:
        return i * multiplier
    return ret
