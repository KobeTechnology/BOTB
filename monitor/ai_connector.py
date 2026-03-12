def get_ai_response():
    responses = {
        "ChatGPT": "Dell Inspiron ranked #2",
        "Gemini": "No Dell product mentioned",
        "Claude": "Dell Inspiron with 16 hour battery"
    }

    for ai, response in responses.items():
        print(f"{ai} Response: {response}")

    return responses

if __name__ == "__main__":
    get_ai_response()
  
