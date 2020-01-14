#!/usr/bin/python3
# This script takes a URL, sends a request to the URL and display X-Request-Id
import sys
from urllib import request

if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as res:
        print(res.getheader("X-Request-Id"))
