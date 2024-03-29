#!/usr/bin/python3
"""script that takes a letter and sends a POST req to URL with letter as param
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    payload = {"q": argv[1][0] if len(argv) > 1 else ""}
    response = requests.post(url, data=payload)
    try:
        res = response.json()
        if not res:
            print("No result")
        else:
            print(f"[{res.get('id')}] {res.get('name')}")
    except ValueError:
        print("Not a valid JSON")
