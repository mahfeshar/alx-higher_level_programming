#!/usr/bin/python3
"""From json string"""
import json


def from_json_string(my_str):
    """an object (Python data structure) represented by a JSON string"""
    return json.loads(my_str)
