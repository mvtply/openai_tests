import os
import openai
import tiktoken
import json

openai.api_key = os.getenv("OPENAI_API_KEY")
model = "gpt-3.5-turbo"
encoding = tiktoken.encoding_for_model(model)

def num_tokens_from_string(string: str, model_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model(model_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens


messages = [
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
print(num_tokens_from_string(json.dumps(messages), model))

'''
completion = openai.ChatCompletion.create(
  model=model,
  messages=messages
)

print(completion.choices[0].message)
'''