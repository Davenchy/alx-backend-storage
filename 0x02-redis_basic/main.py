#!/usr/bin/env python3
"""
Main file
"""
import redis

Cache = __import__('exercise').Cache

cache = Cache()

# Task 0
data = b"hello"
key = cache.store(data)
print(key)

local_redis = redis.Redis()
print(local_redis.get(key))

# Task 1
TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value

# Test cases for get_str and get_int
key = cache.store(b"hello")
assert cache.get_str(key) == "hello"
key = cache.store(123)
assert cache.get_int(key) == 123

# Task 2
cache.store(b"first")
print(cache.get(cache.store.__qualname__))

cache.store(b"second")
cache.store(b"third")
print(cache.get(cache.store.__qualname__))
