import gradio as gr
import openai 
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')


# Define a function that uses the OpenAI API to generate chat responses based on a given message and a history of the conversation.
def predict(message, history):
    history_openai = []
    
    # Populate the history list with user and assistant messages.
    for human, assistant in history:
        history_openai.append({"role": "user", "content": human })
        history_openai.append({"role": "assistant", "content":assistant})
    
    # Append the latest user message to the history.
    history_openai.append({"role": "user", "content": message})
    
    # Make an API call to OpenAI to get the chat completion.
    # The stream=True parameter allows the API to send responses incrementally as text is generated.
    response = openai.ChatCompletion.create(
    messages=history_openai,
    model = "gpt-3.5-turbo",
    stream = True
    )

    partial_message = ""
    for chunk in response:
        # Check if the necessary keys and sub-keys exist in the response chunk
        if 'choices' in chunk and len(chunk['choices']) > 0:
            if 'delta' in chunk['choices'][0] and 'content' in chunk['choices'][0]['delta']:
                
                # Extract the text content from the response and append it to the partial_message.
                text = chunk['choices'][0]['delta']['content']
                partial_message += text
                
                # Yield the growing message to Gradio's interface incrementally.
                yield partial_message  


# Launch a Gradio interface with the predict function.
# The .queue() method is used to manage multiple users by queuing their requests.
gr.ChatInterface(predict).queue().launch()