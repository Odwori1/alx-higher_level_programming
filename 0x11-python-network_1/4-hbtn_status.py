#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status """
import requests

if __name__ == "__main__":
    response = requests.get('https://intranet.hbtn.io/status')
    print(f"Body response:\n"
          f"\t- type: {type(response.text)}\n"
          f"\t- content: {response.text}")
