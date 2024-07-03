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
    },

    # List files in a directory
    {
        "type": "function",
        "function": {
            "name": "list_files",
            "description": "List files in a specified directory",
            "parameters": {
                "type": "object",
                "properties": {
                    "directory": {
                        "type": "string",
                        "description": "The directory to list files from",
                    },
                },
                "required": ["directory"],
            },
        },
    },

    # Create a directory
    {
        "type": "function",
        "function": {
            "name": "create_directory",
            "description": "Create a directory",
            "parameters": {
                "type": "object",
                "properties": {
                    "directory": {
                        "type": "string",
                        "description": "The name of the directory to create",
                    },
                },
                "required": ["directory"],
            },
        },
    },

    # Delete a file
    {
        "type": "function",
        "function": {
            "name": "delete_file",
            "description": "Delete a specified file",
            "parameters": {
                "type": "object",
                "properties": {
                    "filename": {
                        "type": "string",
                        "description": "The name of the file to delete",
                    },
                },
                "required": ["filename"],
            },
        },
    },
]
