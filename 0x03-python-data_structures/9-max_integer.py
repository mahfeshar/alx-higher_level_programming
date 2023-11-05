#!/usr/bin/python3
def max_integer(my_list=[]):
    len_list = len(my_list)
    if len_list == 0:
        return (None)
    max = my_list[0]
    for i in range(1, len_list):
        if my_list[i] > max:
            max = my_list[i]
    return (max)
