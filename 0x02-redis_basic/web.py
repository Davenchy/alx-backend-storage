#!/usr/bin/env python3
""" implement simple cache decorator using redis db """
import requests
import redis
from time import sleep

db = redis.Redis()


def get_page(url: str) -> str:
    """ Fetch the content of a page using its URL """
    # db.incr(f'count:{url}')
    content = db.get(f'content:{url}')
    if content:
        return content.decode('utf-8')
    content = requests.get(url).text
    db.setex(f'content:{url}', 10, content)
    return content


if __name__ == '__main__':
    db.flushdb()
    URL = 'https://github.com'
    get_page(URL)
    sleep(2)
    get_page(URL)
    sleep(3)
    get_page(URL)
    sleep(5)
    get_page(URL)
    count = int(db.get('count:' + URL))
    print(f'Visited {count} times')
