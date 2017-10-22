#!/usr/bin/env python3
import json
import sys


def load_json_data_from_file(filepath):
    with open(filepath) as temp_file:
        return json.load(temp_file)


def pretty_print_json_data(json_data):
    print(json.dumps(json_data, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_file_name = sys.argv[1]
    else:
        input_file_name = input('Input filepath: ')
    json_data = load_json_data_from_file(input_file_name)
    pretty_print_json_data(json_data)
    
