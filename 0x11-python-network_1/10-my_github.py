#!/usr/bin/python3
# This script displays the id of the user
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/user"
    auth = (argv[1], argv[2])
    res = requests.get(url, auth=auth)
    try:
        print(res.json().get("id"))
    except ValueError:
        print("Not a valid JSON")
