tools = [
    # Read from a file
    {
        "type": "function",
        "function": {
            "name": "read_from_file",
            "description": "Read content from a specified file",
            "parameters": {
                "type": "object",
                "properties": {
                    "filename": {
                        "type": "string",
                        "description": "The name of the file to read from",
                    },
                },
                "required": ["filename"],
            },
        },
    },

    # Write to a file
    {
        "type": "function",
        "function": {
            "name": "write_to_file",
            "description": "Write content to a specified file",
            "parameters": {
                "type": "object",
                "properties": {
                    "filename": {
                        "type": "string",
                        "description": "The name of the file",
                    },
                    "content": {
                        "type": "string",
                        "description": "The content to write",
                    },
                },
                "required": ["filename", "content"],
            },
        },
    }
]
