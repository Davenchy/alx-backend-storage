#!/usr/bin/env python3
""" implement simple cache decorator using redis db """
import requests
import redis
from functools import wraps
from typing import Callable

db = redis.Redis()


def count_and_cache(method: Callable) -> Callable:
    """ count and cache function calls """
    @wraps(method)
    def wrapper(url):
        """ inner wrapper function """
        # count calls
        db.incr(f'count:{url}')
        # check if content is cached
        cached = db.get(f'content:{url}')
        if cached:
            return cached.decode('utf-8')
        # fetch content
        content = method(url)
        # cache with expiration time of 10 seconds
        db.setex(f'content:{url}', 10, content)
        return content
    return wrapper


@count_and_cache
def get_page(url: str) -> str:
    """ Fetch the content of a page using its URL """
    return requests.get(url).text


if __name__ == "__main__":
    URL = "https://github.com"
    for _ in range(100):
        get_page(URL)

    count = int(db.get(f"count:{URL}"))
    print(f'Called {count} times')
