def get_ai_responses(prompt, company_profile):
    company = company_profile["company"]
    product = company_profile["product"]

    print(f"Sending prompt to AI assistants: '{prompt}'")
    print(f"Target company: {company}")
    print()

    if company == "Dell":
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

    elif company == "HP":
        responses = [
            {
                "ai_name": "ChatGPT",
                "brand": "HP",
                "product": "HP Pavilion 15",
                "rank": 1,
                "battery_life": "9 hours",
                "price": "$649"
            },
            {
                "ai_name": "Gemini",
                "brand": "HP",
                "product": "HP Pavilion 15",
                "rank": 3,
                "battery_life": "12 hours",
                "price": "$649"
            },
            {
                "ai_name": "Claude",
                "brand": None,
                "product": None,
                "rank": None,
                "battery_life": None,
                "price": None
            }
        ]

    elif company == "Lenovo":
        responses = [
            {
                "ai_name": "ChatGPT",
                "brand": "Lenovo",
                "product": "Lenovo IdeaPad 3",
                "rank": 2,
                "battery_life": "8 hours",
                "price": "$599"
            },
            {
                "ai_name": "Gemini",
                "brand": "Lenovo",
                "product": "Lenovo IdeaPad 3",
                "rank": 1,
                "battery_life": "8 hours",
                "price": "$599"
            },
            {
                "ai_name": "Claude",
                "brand": "Lenovo",
                "product": "Lenovo IdeaPad 3",
                "rank": 3,
                "battery_life": "14 hours",
                "price": "$599"
            }
        ]

    else:
        responses = [
            {
                "ai_name": "ChatGPT",
                "brand": company,
                "product": product,
                "rank": 1,
                "battery_life": "Unknown",
                "price": "Unknown"
            }
        ]

    for response in responses:
        print(response)

    return responses


if __name__ == "__main__":
    sample_company = {
        "company": "Dell",
        "product": "Dell Inspiron 15"
    }

    test_prompt = "Best laptops under $1000"
    get_ai_responses(test_prompt, sample_company)
