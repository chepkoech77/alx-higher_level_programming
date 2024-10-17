#!/usr/bin/python3
"""This scripts saves the command line args in a list and saves in JSON
    in a file, it loads it agein.
"""


import json
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


#Get the command line args
arguments = sys.argv[1:]
filename = "add_item.json"

#Load the existing
existing_list = load_from_json_file(filename)

#Append the existing
existing_list.extend(arguments)

#Save to json
save_to_json_file(existing_list, filename)
