#!/usr/bin/env python3
""" implement simple cache decorator using redis db """
import requests
import redis

db = redis.Redis()
db.flushdb()


def get_page(url: str) -> str:
    """ Fetch the content of a page using its URL """
    db.incr(f'count:{url}')
    content = db.get(f'content:{url}')
    if content:
        return content.decode('utf-8')
    content = requests.get(url).text
    db.set(f'count:{url}', 0)
    db.setex(f'content:{url}', 10, content)
    return content
