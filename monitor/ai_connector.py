def get_ai_responses(prompt):
    print(f"Sending prompt to AI assistants: '{prompt}'")

    responses = [
        {
            "ai_name": "ChatGPT",
            "brand": "Dell",
            "product": "Dell Inspiron 15",
            "rank": 2,
            "battery_life": "10 hours",
            "price": "$699"
        },
        {
            "ai_name": "Gemini",
            "brand": None,
            "product": None,
            "rank": None,
            "battery_life": None,
            "price": None
        },
        {
            "ai_name": "Claude",
            "brand": "Dell",
            "product": "Dell Inspiron 15",
            "rank": 1,
            "battery_life": "16 hours",
            "price": "$699"
        }
    ]

    for response in responses:
        print(response)

    return responses


if __name__ == "__main__":
    test_prompt = "Best laptops under $1000"
    get_ai_responses(test_prompt)
