"""
Example production integration with a real AI API.

This file is included to demonstrate how the monitoring platform
would send standardized shopping prompts to real AI assistants
in a production environment.

This code is not used in the prototype run so the demo remains stable.
"""


# Example: OpenAI API integration
"""
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

def send_prompt_to_openai(prompt):
    response = client.responses.create(
        model="gpt-4.1",
        input=prompt
    )

    return response.output_text
"""


# Example: Anthropic API integration
"""
import anthropic

client = anthropic.Anthropic(api_key="YOUR_API_KEY")

def send_prompt_to_claude(prompt):
    response = client.messages.create(
        model="claude-3-5-sonnet-latest",
        max_tokens=500,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.content[0].text
"""


# Example: Gemini API integration
"""
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

def send_prompt_to_gemini(prompt):
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(prompt)
    return response.text
"""
