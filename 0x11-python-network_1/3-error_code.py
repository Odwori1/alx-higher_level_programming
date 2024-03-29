#!/usr/bin/python3
"""  script that takes in a URL, sends a req to URL and displays the body """
from urllib import request, parse, error
import sys

if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            res = response.read().decode('utf-8')
            print(res)
    except error.HTTPError as err:
        print("Error code:", err.code)
