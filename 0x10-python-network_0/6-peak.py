#!/usr/bin/python3
"""function that finds a peak in a list of unsorted integers"""

def find_peak(list_of_integers):
    numbers = list_of_integers
    left, right = 0, len(numbers) - 1

    if len(numbers) == 0 or numbers is None:
        return None

    while left < right:
        mid = left + (right - left) // 2

        if numbers[mid] > numbers[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return numbers[left]
