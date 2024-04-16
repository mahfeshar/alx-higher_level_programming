#!/usr/bin/python3
def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return 0
    sum = 0
    sumW = 0
    for i in my_list:
        sum += i[0] * i[1]
        sumW += i[1]
    return float(sum) / sumW
