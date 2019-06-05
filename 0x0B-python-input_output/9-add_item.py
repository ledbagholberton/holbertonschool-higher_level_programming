#!/usr/bin/python3
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"
try:
    my_set = load_from_json_file(filename)
except Exception as e:
    my_list = []
    save_to_json_file(my_list, filename)
if len(sys.argv) > 1:
    my_list = load_from_json_file(filename)
    sys.argv.pop(0)
    my_list = my_list + sys.argv
    save_to_json_file(my_list, filename)
