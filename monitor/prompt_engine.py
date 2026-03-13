def generate_prompt(company_profile):
    category = company_profile["category"]
    price_limit = company_profile["price_limit"]

    prompt = f"Best {category} under ${price_limit}"
    print(f"Generated Prompt: {prompt}")
    return prompt


if __name__ == "__main__":
    sample_company = {
        "category": "laptops",
        "price_limit": 1000
    }

    generate_prompt(sample_company)
