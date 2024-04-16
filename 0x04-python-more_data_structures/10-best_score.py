#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    key_best = list(a_dictionary.keys())[0]
    best = a_dictionary[key_best]
    for k, v in list(a_dictionary.items()):
        if v > best:
            best = v
            key_best = k
    return key_best
