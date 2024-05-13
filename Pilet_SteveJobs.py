import openai
from openai import OpenAI

client = OpenAI()


response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": "Can I have a list of product names, that Steve Jobs would come up with, for a pair of shoes that can fit any foot size?"
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
# Extract the response
print(response.choices[0].message.content)
