#!/usr/bin/python3
""" script that takes in a URL and an email and displays the body """
import urllib.parse as parse
import urllib.request as request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = parse.urlencode({"email": email}).encode("ascii")
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        res = response.read().decode("utf-8")
        print(res)
