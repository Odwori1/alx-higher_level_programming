#!/usr/bin/python3
""" script that takes your GitHub cred, uses the GitHub API to display id"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/user"
    credentials = (argv[1], argv[2])
    res = requests.get(url, auth=credentials)
    try:
        print(res.json().get("id"))
    except ValueError:
        print("Not a valid JSON")
