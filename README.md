# gpt-3.5-gradio-chatbot  
An LLM-powered Chatbot app with Gradio.

## How to Run the App
**Note:** OpenAI immediately revokes the API key once it detects that the key has been exposed publicly. Therefore, do not expose your API key.

Generate your OpenAI API key here: [Click Here](https://platform.openai.com/account/api-keys)

### Run Locally
To keep the key private, store it in an environment variable named 'OPENAI_API_KEY' in your OS:   

1. Create a `.env` file and store the key as follows:     
OPENAI_API_KEY='YOUR_API_KEY_HERE'

2. Refer to the key in `app.py` by:
```python
from dotenv import load_dotenv
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
```

3. Ensure openai,Gradio is installed on your system and run the app using the below commands from command prompt:

git clone https://github.com/padmapria/gpt-3.5-gradio-chatbot.git    
cd gpt-3.5-gradio-chatbot    
pip install -r requirements.txt    
python app.py    



