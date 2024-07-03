import json
import os

def read_from_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return json.dumps({"status": "success", "content": content})
    except FileNotFoundError:
        return json.dumps({"status": "error", "message": "File not found"})

def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
    return json.dumps({"status": "success", "message": f"Content written to {filename}"})

def list_files(directory):
    files = os.listdir(directory)
    return json.dumps({"status": "success", "files": files})

def create_directory(directory):
    os.makedirs(directory)
    return json.dumps({"status": "success", "message": f"Directory {directory} created"})

def delete_file(filename):
    try:
        os.remove(filename)
        return json.dumps({"status": "success", "message": f"File {filename} deleted"})
    except FileNotFoundError:
        return json.dumps({"status": "error", "message": "File not found"})
