
__all__ = ['read', 'write']

# - - - - - - - - IMPORTS
import os
import json

# - - - - - - - - GLOBALS
file_name = "daily_routine.json"
file_directory = r"C:\Users\Ishwarya\Documents\GitHub\cornflakes"
file_path = os.path.join(file_directory, file_name)

# - - - - - - - - METHODS
def _get_dictionary(data):
    write_data = {}
        
    data = data.replace(" ", "")
    array_data = data.split(',')

    for i in range(len(array_data)):
        text = array_data[i]
        if text.lower() == "clockin":
            write_data["clockin"] = array_data[i+1]
        elif text.lower() == "clockout":
            write_data["clockout"] = array_data[i+1]
        elif text.lower() == "takebreak":
            write_data["takebreak"] = array_data[i+1]
        elif text.lower() == "endbreak":
            write_data["endbreak"] = array_data[i+1]
    
    return write_data

def read():
    global file_path

    if not os.path.exists(file_path):
        with open(file_path, 'wt') as file:
            json.dump({"key" : "value"}, file)
    
    data = {}
    with open(file_path, 'rt') as file:
        data = json.load(file)
    
    return data

def write(new_data):
    global file_path

    if isinstance(new_data, str):
        new_data = _get_dictionary(new_data)

    data = read()
    data.update(new_data)

    if isinstance(data, dict):
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)

