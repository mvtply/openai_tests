import os
import openai
openai.organization = "org-HqxhElREZ1F4BKsfH5w4P8IO"
openai.api_key = "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"
x = openai.Model.list()
print(x)