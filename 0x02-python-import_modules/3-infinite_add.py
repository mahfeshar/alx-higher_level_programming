#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    sumi = 0;
    for i in range(1, len(argv)):
        sumi += int(argv[i])
    print(sumi)
