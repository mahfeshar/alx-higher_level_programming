#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        value = fct(*args)
        return value
    except Exception:
        print('Exception: {}'.format(sys.exc_info()[1]), file=sys.stderr)
        return None
