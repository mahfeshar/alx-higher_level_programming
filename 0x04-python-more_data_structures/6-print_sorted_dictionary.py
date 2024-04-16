#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dicKeys = sorted(a_dictionary)
    for i in dicKeys:
        print(f'{i}: {a_dictionary[i]}')
