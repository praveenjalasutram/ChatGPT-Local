import openai
import tkinter as tk

# Set the OpenAI API key
openai.api_key = "YOUR_API_KEY_HERE" # Note: You have to pay for this service upon completion of the free trial.

# Create a function to handle the search query
def search():
    # Get the search query from the user input field
    query = user_input.get()

    # Use the chatbot model to generate a response
    response = openai.Completion.create(engine="text-davinci-002", prompt=query, max_tokens=1024, temperature=0.5)

    # Get the response text
    response_text = response["choices"][0]["text"]

    # Display the response in the GUI
    result_label.config(text=response_text)

# Create the main window
window = tk.Tk()
window.title("ChatGPT Local ChatBot, Created by: CyberSec_Sai")
# window.attributes('-fullscreen', True) # For Full screen
window.geometry('1920x1080')  # Fit the window to the size of the screen

# Create a label and an input field for the search query
query_label = tk.Label(text="Enter your search query:")
query_label.pack()
user_input = tk.Entry()
user_input.pack()

# Create a button to submit the search query
search_button = tk.Button(text="Search", command=search)
search_button.pack()

# Create a label to display the result
result_label = tk.Label(text="")
result_label.pack()

# Create a label to display the Creator
creator_label = tk.Label(text='Created by CyberSec_Sai:\nWebsite: https://praveenjalasutram.wixsite.com/praveenjalasutram\nLinkedIn: https://www.linkedin.com/in/praveenjalasutram/\nTwitter: https://twitter.com/cybersec_sai\nGitHub: https://github.com/praveenjalasutram')
#creator_label.grid(row=4, column=1)

# Run the GUI
window.mainloop()
