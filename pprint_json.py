#!/usr/bin/env python3
"""Read data from JSON file and print to stdout in a pretty manner"""
import json
import sys


def load_data(filepath):
    """Returns string loaded from JSON file"""
    with open(filepath) as f:
        return json.load(f)


def pretty_print_json(data):
    """Converts string data to JSON and prints it in a pretty manner"""
    print(json.dumps(data, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        file_name = input('Input filepath: ')
    pretty_print_json(load_data(file_name))
    
