import os
import openai
import json
from custfunct import num_tokens_from_messages

openai.api_key = os.getenv("OPENAI_API_KEY")
model = "gpt-3.5-turbo"
messages = [
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
  
print(f"{num_tokens_from_messages(messages, model)} prompt tokens counted by num_tokens_from_messages().")

response = openai.ChatCompletion.create(
  model=model,
  messages=messages
)
print(response.choices[0].message)
print(f'{response["usage"]["prompt_tokens"]} prompt tokens counted by the OpenAI API.')