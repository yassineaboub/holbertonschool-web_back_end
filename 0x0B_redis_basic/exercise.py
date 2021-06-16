#!/usr/bin/env python3
"""Redis basic module
"""
from typing import Union, Callable, Optional
import redis
import uuid
import sys
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """create and return function that increments the count
    for that key every time the method is called and returns
    the value returned by the original method.
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """ wrapp function
        """
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    store the history of inputs and outputs
    for a particular function.
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args):
        """ wrap function
        """
        self._redis.rpush("{}:inputs".format(key), str(args))
        result = method(self, *args)
        self._redis.rpush("{}:outputs".format(key),
                          str(result))
        return result
    return wrapper


def replay(method: Callable):
    """
    displays nthe history of calls
    """
    r = method.__self__._redis
    method_name = method.__qualname__

    inputs = r.lrange("{}:inputs".format(method_name), 0, -1)
    outputs = r.lrange("{}:outputs".format(method_name), 0, -1)

    print("{} was called {} times:".format(method_name,
          r.get(method_name).decode("utf-8")))
    for i, o in tuple(zip(inputs, outputs)):
        print("{}(*('{}',)) -> {}".format(method_name, i.decode("utf-8"),
              o.decode("utf-8")))


class Cache:
    """
    cache class
    """

    def __init__(self):
        """
        init
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Takes a data argument and returns a string. The method
        should generate a random key (e.g. using uuid)
        """
        key = str(uuid.uuid1())
        self._redis.set(key, data)
        return key

    def get(self,
            key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """  Reading from Redis and recovering original type
        """
        res = self._redis.get(key)
        return fn(res) if fn else res

    def get_str(self, data: bytes) -> str:
        """converts bytes to string.
        """
        return data.decode('utf-8')

    def get_int(self, data: bytes) -> int:
        """converts bytes to int.
        """
        return int.from_bytes(data, sys.byteorder)
