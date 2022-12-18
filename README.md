# ChatGPT Local Chatbot
This script allows you to search a chatbot using a GUI. It uses the OpenAI API and the openai Python library to interact with the Chatbot API, and the tkinter library to create the GUI.

## Prerequisites
- Python 3.x
- The openai library: `pip install openai`
- A valid OpenAI API key. You can sign up for an API key and learn more about the Chatbot API at https://beta.openai.com/docs/api-reference/completion/create.

## How it works
This script uses the openai library to interact with the Chatbot API, and the tkinter library to create a simple GUI.

To use this script, you will need to sign up for an OpenAI API key and replace "YOUR_API_KEY_HERE" with your own API key. You can sign up for an API key and learn more about the Chatbot API at https://beta.openai.com/docs/api-reference/completion/create.

## Usage
- Replace "YOUR_API_KEY_HERE" in the following line with your own API key:

  `openai.api_key = "YOUR_API_KEY_HERE"`

- Run the script: `python3 chatgpt_local_chatbot.py`
- Enter your search query in the input field and click the "Search" button.
The chatbot's response will be displayed in the result label.

## Customization
You can customize the behavior of the chatbot by modifying the following parameters in the openai.Completion.create() function:

- **engine**: The name of the chatbot model to use.
- **prompt**: The search query to send to the chatbot.
- **max_tokens**: The maximum number of tokens (words) in the chatbot's response.
- **temperature**: Controls the creativity of the chatbot's response. A value of 0 will generate a more predictable response, while a value greater than 0 will generate a more creative and varied response.

You can also customize the appearance and behavior of the GUI by modifying the code in the tkinter section of the script.

I hope this helps! Let me know if you have any questions or if you need further assistance.
