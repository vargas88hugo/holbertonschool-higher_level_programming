#!/usr/bin/python3
# This script prints the response of the request and handle errors
from sys import argv
import requests


if __name__ == "__main__":
    res = requests.get(argv[1])
    if res.status_code > 400:
        print("Error code:", res.status_code)
    else:
        print(res.text)
