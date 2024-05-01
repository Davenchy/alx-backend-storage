#!/usr/bin/env python3
""" Using redis in python """
import redis
import uuid
from typing import Union


class Cache:
    """ Cache Class """

    def __init__(self):
        """ initialize redis cache object """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Cache/store data """
        key = str(uuid.uuid1())
        self._redis.set(key, data)
        return key
