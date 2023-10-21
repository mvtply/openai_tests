import os
import openai
openai.organization = "org-HqxhElREZ1F4BKsfH5w4P8IO"
openai.api_key = os.getenv("OPENAI_API_KEY")
x = openai.Model.list()
print(x)