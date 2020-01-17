#!/usr/bin/python3
# This script consumes a Star War API and search characters
from sys import argv
import requests

if __name__ == "__main__":
    params = {"search": argv[1]}
    url = "http://swapi.co/api/people/?search="
    res = requests.get(url, params=params)
    try:
        d = res.json()
        print("Number of results:", d.get("count"))
        for result in d.get("results"):
            print(result.get("name"))
    except ValueError:
        print("Not a valid JSON")
