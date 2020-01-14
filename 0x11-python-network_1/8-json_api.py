#!/usr/bin/python3
# This script sends a letter to a POST request
from sys import argv
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(argv) > 1:
        data = {"q": argv[1][0]}
    else:
        data = None
    res = requests.post(url, data=data)
    try:
        d = res.json()
        if not d:
            print("No result")
        else:
            print("[{}] {}".format(d.get("id"), d.get("name")))
    except ValueError:
        print("Not a valid JSON")
