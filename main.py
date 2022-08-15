"""Docstring for main.py"""
import time
import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host="redis", port=6379)


def get_hit_count():
    """Times the page has been visited"""
    retries = 5
    while True:
        try:
            return cache.incr("hits")
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route("/")
def hello():
    """Root route of Flask app"""
    count = get_hit_count()
    return f"Yooo from Docker! I have been seen {count} times.\n"
