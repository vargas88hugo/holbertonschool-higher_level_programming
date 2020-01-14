#!/usr/bin/python3
# Script that takes an URL, sends a POST and display the body of response
from sys import argv
import requests


if __name__ == "__main__":
    response = requests.post(argv[1], data={'email': argv[2]})
    print(response.text)
