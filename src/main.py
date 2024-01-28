import sys

from LsRtoJson import LsRtoJson

import os
import json


# https://www.geeksforgeeks.org/create-a-json-representation-of-a-folder-structure/
def create_folder_structure_json(path):
    # Initialize the result dictionary with folder
    # name, type, and an empty list for children
    result = {'name': os.path.basename(path),
              'type': 'folder', 'children': []}

    # Check if the path is a directory
    if not os.path.isdir(path):
        return result

        # Iterate over the entries in the directory
    for entry in os.listdir(path):
        # Create the full path for the current entry
        entry_path = os.path.join(path, entry)

        # If the entry is a directory, recursively call the function
        if os.path.isdir(entry_path):
            result['children'].append(create_folder_structure_json(entry_path))
            # If the entry is a file, create a dictionary with name and type
        else:
            result['children'].append({'name': entry, 'type': 'file'})

    return result


def test_1(folder_path):
    # Specify the path to the folder you want to create the JSON for
    # folder_path = '/path/to/folder'

    # Call the function to create the JSON representation
    folder_json = create_folder_structure_json(folder_path)

    # Convert the dictionary to a JSON string with indentation
    folder_json_str = json.dumps(folder_json, indent=4)

    # Print the JSON representation of the folder structure
    print(folder_json_str)

    # Specify the path to the output file
    output_file = '/tmp/output.json'

    # Save the JSON representation of a folder structure
    with open(output_file, 'w') as f:
        # Write the JSON string to the file
        f.write(folder_json_str)

    # Print a confirmation message with the output file path
    print("JSON saved to", output_file)


def test_2():
    print("Started")
    obj = LsRtoJson()
    lines = obj.read_file("../test/T5-FamVideo.txt")
    obj.create_json(lines, skip_lines=8)


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print(F"Usage: {sys.argv[0]} [path_to_check]")
    else:
        test_1(sys.argv[1])
