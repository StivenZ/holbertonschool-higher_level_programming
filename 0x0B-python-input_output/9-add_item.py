#!/usr/bin/python3
"""Module handling arguments to JSON files"""
import json
import sys
import os.path
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


filename = "add_item.json"
if os.path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []
for ar in range(len(sys.argv)):
    if ar != 0:
        my_list.append(sys.argv[ar])
save_to_json_file(my_list, filename)
