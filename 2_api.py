"""
Close source-
1. OpenAI
2. Anthropic
3. Cohere
4. Google Gemini
5. Microsoft Azure OpenAI
6. Grok

How to use the API(Application Programable Interface) key
1. Pass the API key directly when creating the Chatbot instance.
   Example: chatbot = Chatbot(api_key="your_api_key_here")

2. Store the API key in an environment variable and let the Chatbot class read it automatically.
   Example: os.environ["OPENAI_API_KEY"] = "your_api_key_here"

3. Store the API key in a .env/config.ini file in the same directory as your script.
   Example content of .env file: 
    OPENAI_API_KEY= os.getenv("OPENAI_API_KEY")
"""

# pip install python-dotenv

from dotenv import load_dotenv
import os
# used to check api key is present or not
#print(load_dotenv())
# it retuens api keym
#print(os.getenv('secret_key'))
load_dotenv()
from openai import OpenAI
api_key = os.getenv("OPENAI_API_KEY")

chatbot = OpenAI(api_key=api_key)

chatbot_response = chatbot.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "What is Data Science?"}
    ]
)
print(chatbot_response.choices[0].message.content)

# api_key = os.getenv("OPENAI_API_KEY")
# print(api_key)

#--------------------------------------
# from openai import OpenAI
# client = OpenAI()

# response = client.responses.create(
#     model="gpt-4o-mini",
#     input=[
#         {
#             "role": "user",
#             "content": [
#                 {
#                     "type": "input_text",
#                     "text": "Please explain this image?",
#                 }, 
#                 {
#                     "type": "input_image",
#                     "image_url": "https://wallpapercave.com/wp/teRdoI4.jpg"
#                 }
#             ]
#         }
#     ]
# )

# print(response.output_text)
#--------------------------------------------------
# pip install openai
# from openai import OpenAI
# api_key = os.getenv("OPENAI_API_KEY")

# chatbot = OpenAI(api_key=api_key)
# question = "What is AgenticAI?"
# response = chatbot.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": question},
#     ],
# )
# print(response.choices[0].message.content)
#print(response)