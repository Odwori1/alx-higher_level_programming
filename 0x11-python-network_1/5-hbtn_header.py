#!/usr/bin/python3
""" script that takes in a URL, sends a req to URL and displays the value """
import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get(argv[1])
    data = response.headers.get('X-Request-Id')
    print(data)
