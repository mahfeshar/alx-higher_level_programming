#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sumi = 0;
    for i in range(1, len(argv)):
        sumi += int(argv[i])
    print(sumi)
