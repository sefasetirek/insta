import openai
from openai import OpenAI

client = OpenAI(api_key=openai.api_key)

def generate_content(prompt, max_tokens=1000):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Sen bir sosyal medya içerik uzmanısın."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_tokens
    )
    return response.choices[0].message.content

