#!/usr/bin/python3
# This script takes an URL, sends a request and displays X-Request-id
from sys import argv
import requests


if __name__ == "__main__":
    res = requests.get(argv[1])
    print(res.headers.get('X-Request-Id'))
