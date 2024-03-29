#!/usr/bin/python3
"""script that takes a URL and email address, sends a POST req to the URL """
import requests
from sys import argv

if __name__ == "__main__":
    response = requests.post(argv[1], data={'email': argv[2]})
    res = response.text
    print(res)
