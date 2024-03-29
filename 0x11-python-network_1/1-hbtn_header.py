#!/usr/bin/python3
""" script that takes in a URL and displays the value of the X-Request-Id """
import urllib.request as request
import sys


if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as response:
        value = response.info()
        print(value.get("X-Request-Id"))
