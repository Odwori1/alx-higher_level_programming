#!/usr/bin/python3
"""Imported module for adding items to a JSON file"""
import sys
import json
import os.path

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

json_file = "add_item.json"
arr = []

if os.path.exists(json_file):
    arr = load_from_json_file(json_file)

for arg in range(1, len(sys.argv)):
    arr.append(sys.argv[arg])

save_to_json_file(arr, json_file)
