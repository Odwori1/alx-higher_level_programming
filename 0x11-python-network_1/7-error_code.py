#!/usr/bin/python3
""" script that takes a URL, sends a req to URL and displays the body res"""
from sys import argv
import requests

if __name__ == "__main__":
    response = requests.get(argv[1])
    if response.status_code > 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
