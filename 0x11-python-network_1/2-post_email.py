#!/usr/bin/python3
# This script takes an URL and an email, sends a POST request to the URL
import sys
from urllib import request, parse

if __name__ == "__main__":
    data = parse.urlencode({"email": sys.argv[2]}).encode()
    print(data)
    with request.urlopen(sys.argv[1], data) as res:
        print(res.read().decode('utf-8'))
