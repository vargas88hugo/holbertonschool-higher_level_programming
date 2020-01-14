#!/usr/bin/python3
# This script print the response and catch the error
import sys
from urllib import request, parse, error

if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code:", e.code)
