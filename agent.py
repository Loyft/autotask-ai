import os
import json

from dotenv import load_dotenv
from openai import OpenAI
from config import *
from utils import read_from_file, write_to_file
from tools import tools

load_dotenv()
client = OpenAI(api_key=os.getenv('API_KEY'))

def run_conversation(message, messages, model="gpt-3.5-turbo"):
    # Append the user input (message) to the messages history
    messages.append(message)

    content = message['content'].strip().lower()
    
    # Handling commands
    if content.startswith('/'):
        if content == '/gpt3':
            model = "gpt-3.5-turbo"
            print("Switched to GPT-3-turbo.")
        elif content == '/gpt4':
            model = "gpt-4"
            print("Switched to GPT-4.")
        elif content == '/gpt':
            print(f"Current model is: {model}")
        else:
            print("Invalid command.")

        # Request new input after handling command
        user_input = input(LIGHT_GREEN + "\nUSER: ")
        message = {
            "role": "user",
            "content": user_input
        }
        run_conversation(message, messages, model)
        return

    if content == 'exit':
        print(LIGHT_YELLOW + "GPT: Goodbye! 👋" + RESET)
        return

    # Call to the AI model
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        tools=tools,
        tool_choice="auto",
    )

    response_message = response.choices[0].message

    # If tool calls are requested, handle them
    tool_calls = response_message.tool_calls
    if tool_calls:
        handle_tool_calls(tool_calls, messages, model, response_message)
    else:
        process_user_input(response, messages, model)

def handle_tool_calls(tool_calls, messages, model, response_message):
    available_functions = {
        "read_from_file": read_from_file,
        "write_to_file": write_to_file,
    }
    messages.append(response_message)

    for tool_call in tool_calls:
        function_name = tool_call.function.name
        function_to_call = available_functions[function_name]
        function_args = json.loads(tool_call.function.arguments)
        function_response = function_to_call(**function_args)
        print(DARK_VIOLET + f"--> {function_name}" + RESET)
        messages.append({
            "tool_call_id": tool_call.id,
            "role": "tool",
            "name": function_name,
            "content": function_response,
        })

    second_response = client.chat.completions.create(
        model=model,
        messages=messages,
    )
    process_user_input(second_response, messages, model)

def process_user_input(response, messages, model):
    token_info = f" ({response.usage.total_tokens} Tokens)"
    user_input = input(DARK_YELLOW + "GPT:" + RESET + LIGHT_YELLOW + f" {response.choices[0].message.content}{token_info}\n" + DARK_GREEN + "USER: " + RESET + LIGHT_GREEN)
    if user_input.strip().lower() == 'exit':
        print(LIGHT_YELLOW + "GPT: Goodbye! 👋" + RESET)
        return
    else:
        message = {
            "role": "user",
            "content": user_input
        }
        run_conversation(message, messages, model)

# Initial setup
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
