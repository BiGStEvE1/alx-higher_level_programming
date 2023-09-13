#!/usr/bin/python3
""" creates an Object from a JSON file
"""
import json


def load_from_json_file(filename):
    """ Function that creates an Object from a JSON file

    Raises:
        Exception: when the object can't be encoded

    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
