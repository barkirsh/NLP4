from openai import OpenAI

import os

# api_key = os.getenv("OPENAI_API_KEY_BARDRIVE")


# Retrieve the API key from environment variables
api_key = os.getenv("OPENAI_API_KEY_BARDRIVE")
if not api_key:
    raise ValueError("API key is missing. Please set OPENAI_API_KEY_BARDRIVE in your environment variables.")

# Initialize the OpenAI client
client = OpenAI(api_key=api_key)

# Make a request to OpenAI's API
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
        {"role": "user", "content": "write a haiku about AI"}
    ]
)

# Print the completion
print(completion.choices[0].message["content"])
