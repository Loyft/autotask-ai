from dotenv import load_dotenv
from openai import OpenAI
import json
import os

# ANSI color codes
DARK_GREEN = '\033[32m'  # Darker green
LIGHT_GREEN = '\033[92m'  # Light green
DARK_YELLOW = '\033[33m'  # Darker yellow
LIGHT_YELLOW = '\033[93m'  # Light yellow
DARK_VIOLET = '\033[35m'  # Dark violet
LIGHT_VIOLET = '\033[95m'  # Light violet
RESET = '\033[0m'
BOLD = '\033[1m'

load_dotenv()
client = OpenAI(api_key=os.getenv('API_KEY'))

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

def run_conversation(message, messages):
    # Append the user input (message) to the messages history
    messages.append(message)

    if message['content'].strip().lower() == 'exit':
        print(LIGHT_YELLOW + "GPT: Goodbye! 👋" + RESET)
        return

    tools = [
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

    # Make the first call to see if it requires any tool calls
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        tools=tools,
        tool_choice="auto",
    )

    # isolate the message from the response
    response_message = response.choices[0].message

    # isolate the tool calls from the response
    tool_calls = response_message.tool_calls

    # If tool calls are requested, run the tool calls and continue the conversation
    if tool_calls:
        available_functions = {
            "read_from_file": read_from_file,
            "write_to_file": write_to_file,
        }
        messages.append(response_message)

        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_to_call = available_functions[function_name]
            function_args = json.loads(tool_call.function.arguments)

            # Call the function and save the response in function_response
            function_response = function_to_call(**function_args)
            print(DARK_VIOLET + f"CALLING FUNCTION: {function_name}" + RESET)

            # Append the function_response to the messages history
            messages.append({
                "tool_call_id": tool_call.id,
                "role": "tool",
                "name": function_name,
                "content": function_response,
            })

        # Make Second call with the response from the tool calls
        second_response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )

        # Append the second response to the messages history
        token_info = f" ({second_response.usage.total_tokens} Tokens)"
        user_input = input(DARK_YELLOW + "GPT:" + RESET + LIGHT_YELLOW + f" {second_response.choices[0].message.content}{token_info}\n" + DARK_GREEN + "USER: " + RESET + LIGHT_GREEN)
        if user_input.strip().lower() == 'exit':
            print(LIGHT_YELLOW + "GPT: Goodbye! 👋" + RESET)
            return
        else:
            message = {
                "role": "user",
                "content": user_input
            }
            run_conversation(message, messages)

    # If no tool calls are requested, continue the conversation with normal GPT
    else:
        token_info = f" ({response.usage.total_tokens} Tokens)"
        user_input = input(DARK_YELLOW + "GPT:" + RESET + LIGHT_YELLOW + f" {response_message.content}{token_info}\n" + DARK_GREEN + "USER: " + RESET + LIGHT_GREEN)
        if user_input.strip().lower() == 'exit':
            print(LIGHT_YELLOW + "GPT: Goodbye! 👋" + RESET)
            return
        else:
            message = {
                "role": "user",
                "content": user_input
            }
            run_conversation(message, messages)

# Setup and initial messages
messages = [
    {
        "role": "system",
        "content": "You are an AI Assistant that can answer any question by using function calls. Answer the questions you are asked as good as possible and tell what you've done. Use a friendly tone and emojis to make the conversation more engaging. 😊"
    }
]

user_message = input(DARK_YELLOW + "GPT: Hi! How may I assist you today? 😊\n" + RESET + LIGHT_GREEN + "USER: ")
message = {
    "role": "user",
    "content": user_message
}

run_conversation(message, messages)
