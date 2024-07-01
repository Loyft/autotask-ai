# AI Chatbot Agent

## Overview
This repository contains an AI Chatbot Agent designed to interact with the user via the command-line interface. The chatbot utilizes OpenAI's GPT model to generate responses and carry out tasks such as reading from and writing to files. The chatbot dynamically integrates with the OpenAI API to fetch and compute responses based on user inputs and predefined functions.

## Features
- **Dynamic Conversation Handling:** Leverages OpenAI's GPT-3.5-turbo to handle conversations, making appropriate API and function calls as required.
- **File Operations:** Includes functions to read from and write to files, enabling data retrieval and storage during interactions.
- **ANSI Color Coding:** Enhances the CLI experience by using ANSI color codes to differentiate between user inputs, GPT responses, and function calls.

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

2. **Environment Setup** 

   Ensure you have Python installed on your machine, and then set up a virtual environment:
   ```
   python3 -m venv venv
   ```
   Activate the virtual environment:
   ```
   source venv/bin/activate
   ``` 
   (On Windows use `venv\Scripts\activate`)

3. **Install Dependencies** 

   Install necessary Python packages:
   ```
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables** 

   Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   API_KEY=your_openai_api_key_here
   ```

5. **Run the Chatbot**
   ```
   python3 agent.py
   ```

6. **Exit the Chatbot** 

   To exit the Chat type `exit` when asked for a prompt.



## Contributing
Contributions are welcome! If you have suggestions or improvements, feel free to fork the repository and submit a pull request. 😊

## License
Distributed under the MIT License. See `LICENSE` for more information.

