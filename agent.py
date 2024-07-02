import os
import json

from dotenv import load_dotenv
from openai import OpenAI
from config import *
from utils import read_from_file, write_to_file
from tools import tools

load_dotenv()
client = OpenAI(api_key=os.getenv('API_KEY'))

def calculate_cost(response, model):
    prompt_tokens = response.usage.prompt_tokens
    completion_tokens = response.usage.completion_tokens

    if 'gpt-4o' in model:
        # gpt-4o pricing
        input_cost = prompt_tokens * 5.00 / 1000000
        output_cost = completion_tokens * 15.00 / 1000000
    else:
        # GPT-3 pricing
        input_cost = prompt_tokens * 0.50 / 1000000
        output_cost = completion_tokens * 1.50 / 1000000

    total_cost = input_cost + output_cost
    return total_cost

def cost_color(total_cost):
    if total_cost < 0.01:
        return LIGHT_GREEN + f"${total_cost:.6f}" + RESET
    elif total_cost < 0.10:
        return LIGHT_YELLOW + f"${total_cost:.6f}" + RESET
    else:
        return RED + f"⚠️ ${total_cost:.6f}" + RESET

def run_conversation(message, messages, model="gpt-3.5-turbo"):
    messages.append(message)

    content = message['content'].strip().lower()

    # Handling commands
    if content.startswith('/'):
        if content == '/gpt3':
            model = "gpt-3.5-turbo"
            print(LIGHT_GREEN + "Switched to GPT-3-turbo." + RESET)
        elif content == '/gpt4':
            model = "gpt-4o"
            print(LIGHT_GREEN + "Switched to gpt-4o." + RESET)
        elif content == '/gpt':
            print(LIGHT_GREEN + f"Current model is: {model}" + RESET)
        else:
            print(LIGHT_GREEN + "Invalid command." + RESET)

        user_input = input(LIGHT_GREEN + "\nUSER: " + RESET)
        message = {
            "role": "user",
            "content": user_input
        }
        run_conversation(message, messages, model)
        return

    if content == 'exit':
        print(LIGHT_YELLOW + "GPT: Goodbye! 👋" + RESET)
        return

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        tools=tools,
        tool_choice="auto",
    )

    response_message = response.choices[0].message
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
    token_info = f" {response.usage.total_tokens} Tokens"
    cost = calculate_cost(response, model)
    cost_display = cost_color(cost)
    user_input = input(DARK_YELLOW + "GPT:" + RESET + LIGHT_YELLOW + f" {response.choices[0].message.content} ({token_info} - {cost_display})\n" + DARK_GREEN + "USER: " + RESET + LIGHT_GREEN)
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
