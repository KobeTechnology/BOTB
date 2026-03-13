def check_ai_responses(parsed_responses, official_data):
    """
    Compares AI responses with official product data
    and detects hallucinations or inaccuracies.
    """

    results = []

    for response in parsed_responses:

        brand_mentioned = response["brand"] == official_data["company"]

        accuracy_status = "N/A"

        if brand_mentioned:

            if response["battery_life"] != official_data["battery_life"]:
                accuracy_status = "Hallucination Detected"

            else:
                accuracy_status = "Correct"

        result = {
            "ai_name": response["ai_name"],
            "brand_mentioned": brand_mentioned,
            "rank": response["rank"],
            "accuracy_status": accuracy_status
        }

        results.append(result)

    return results
