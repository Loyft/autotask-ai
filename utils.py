import json

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
