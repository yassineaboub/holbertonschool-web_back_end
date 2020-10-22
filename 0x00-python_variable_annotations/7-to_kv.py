#!/usr/bin/env python3
"""string int float to tuple function"""


from typing import Callable, Iterator, Union, Optional, List, Tuple

def to_kv(k : str,v: Union[int, float]) -> Tuple[str,float]:
    return (k, v**2)
