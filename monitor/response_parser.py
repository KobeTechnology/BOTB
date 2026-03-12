def parse_ai_responses(raw_responses):
    """
    Converts raw AI responses into structured monitoring data.
    """

    parsed_responses = []

    for response in raw_responses:
        parsed = {
            "ai_name": response.get("ai_name"),
            "brand": response.get("brand"),
            "product": response.get("product"),
            "rank": response.get("rank"),
            "battery_life": response.get("battery_life"),
            "price": response.get("price")
        }

        parsed_responses.append(parsed)

    return parsed_responses


if __name__ == "__main__":
    sample = [
        {
            "ai_name": "ChatGPT",
            "brand": "Dell",
            "product": "Dell Inspiron 15",
            "rank": 2,
            "battery_life": "10 hours",
            "price": "$699"
        }
    ]

    print(parse_ai_responses(sample))
