#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sumi = 0;
    for i in sys.argv:
        sumi += int(i)
    print(sumi)
