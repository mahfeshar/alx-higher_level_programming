#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    best = a_dictionary[list(a_dictionary)[0]]
    for i in a_dictionary:
        if a_dictionary[i] > best:
            best = a_dictionary[i]
            key_best = i
    return key_best
