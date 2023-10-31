#!/usr/bin/python3
rev = 0;
for i in range(90, 64, -1):
    if rev == 0:
        char = 32
        rev ^= 1
    else:
        char = 0
        rev ^= 1
    print("{}".format(chr(i + char)), end='')
