#!/usr/bin/env python3
""" Using redis in python """
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps

DataTypes = Union[str, bytes, int, float]
ConversionFn = Callable[[bytes], DataTypes]


def count_calls(method: Callable) -> Callable:
    """ count function calls """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ inner wrapper function """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """ Cache Class """

    def __init__(self):
        """ initialize redis cache object """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: DataTypes) -> str:
        """ Cache/store data """
        key = str(uuid.uuid1())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> DataTypes:
        """ get data from cache """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """ get data from cache as string """
        return self.get(key, lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """ get data from cache as integer """
        return self.get(key, int)
