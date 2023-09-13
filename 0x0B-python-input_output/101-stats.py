#!/usr/bin/python3
"""Imported module"""
import sys
from collections import defaultdict

"""script that reads stdin line by line and computes metrics"""
file_size = 0
status_counts = defaultdict(int)
count = 0

try:
    for line in sys.stdin:
        count += 1

        parts = line.strip().split(" ")
        status_code = parts[-2]
        file_size += int(parts[-1])
        status_counts[status_code] += 1

        if count % 10 == 0:
            print("File_size:", file_size)
            for code in sorted(status_counts.keys()):
                print(f"{code}: {status_counts[code]}")
            print()

except KeyboardInterrupt:
    print("File_size:", file_size)
    for code in sorted(status_counts.keys()):
        print(f"{code}: {status_counts[code]}")
    print()

if count < 10:
    print("File_size:", file_size)
    for code in sorted(status_counts.keys()):
        print(f"{code}: {status_counts[code]}")
