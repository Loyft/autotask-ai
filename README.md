# AI Chatbot Agent

## Overview
This repository contains an AI Chatbot Agent designed to interact with the user via the command-line interface. The chatbot utilizes OpenAI's GPT model to generate responses and carry out tasks such as reading from and writing to files and more. The chatbot dynamically integrates with the OpenAI API to fetch and compute responses based on user inputs and predefined functions.

## Showcase
Creating a ToDo-List Website (gpt-4o-mini)

https://github.com/Loyft/autotask-ai/assets/67104490/98b9764b-5e62-4e15-a317-e0a3393a6bfb


## Features
- **Dynamic Conversation Handling:** Leverages OpenAI's GPT Models to handle conversations, making appropriate API and function calls as required.
- **File Operations:** Includes functions to read from and write to files, enabling data retrieval and storage during interactions. Can also create directories, list files in a given directory and delete files (use with caution).
- **ANSI Color Coding:** Enhances the CLI experience by using ANSI color codes to differentiate between user inputs, GPT responses, and function calls.

## Flowchart

<img width="767" alt="Screenshot 2024-07-03 at 14 04 39" src="https://github.com/Loyft/autotask-ai/assets/67104490/bdec5083-5dcb-4efb-be55-7c23e6692f3a">


## Setup
To run this chatbot on your local machine, follow these steps:

1. **Clone the Repository**
   ```
   git clone https://github.com/loyft/autotask-ai.git
   ```
   Navigate to the project directory:
   ```
   cd autotask-ai
   ```


2. **Install Dependencies** 

   Install necessary Python packages:
   ```
   pip install -r requirements.txt
   ```
   or
   ```
   pip3 install -r requirements.txt
   ```

3. **Set Up Environment Variables** 

   Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   API_KEY=your_openai_api_key_here
   ```

4. **Run the Chatbot**
   ```
   python agent.py
   ```
   or
   ```
   python3 agent.py
   ```

## Usage

1. **Change GPT Model**

   Use commands via `/` to change the current GPT model.

   `/gpt`  to display the currently active GPT model.

   `/gpt3` to use gpt-3.5-turbo

   `/gpt4` to use gpt-4o

   `/gpt4-mini` to use gpt-4o-mini (default)

2. **Usage Cost**

   Displays the Token usage and total cost of the response (prompt + completion)

3. **Exit the Chatbot** 

   To exit the Chat type `exit` when asked for a prompt.

## Contributing
Contributions are welcome! If you have suggestions or improvements, feel free to fork the repository and submit a pull request. 😊

## License
Distributed under the MIT License. See `LICENSE` for more information.

