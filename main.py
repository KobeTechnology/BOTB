from config.company_profile import COMPANY_PROFILE
from monitor.prompt_engine import generate_prompt
from monitor.ai_connector import get_ai_responses
from monitor.response_parser import parse_ai_responses
from api.product_data_api import get_product_data
from monitor.hallucination_checker import check_ai_responses
from monitor.metrics_tracker import calculate_metrics


def main():
    print("Step 1: Loading company profile...")
    print(COMPANY_PROFILE)
    print()

    print("Step 2: Generating shopping prompt...")
    prompt = generate_prompt(COMPANY_PROFILE)
    print()

    print("Step 3: Pulling official product data...")
    official_data = get_product_data(COMPANY_PROFILE)
    print(f"Official Product Data: {official_data}")
    print()

    print("Step 4: Collecting AI responses...")
    raw_ai_responses = get_ai_responses(prompt)
    print()

    print("Step 5: Parsing AI responses...")
    parsed_responses = parse_ai_responses(raw_ai_responses)
    for response in parsed_responses:
        print(response)
    print()

    print("Step 6: Running hallucination and visibility checks...")
    results = check_ai_responses(parsed_responses, official_data)
    print()

    print("Step 7: Calculating metrics...")
    metrics = calculate_metrics(results)
    print(metrics)
    print()

    print("Step 8: Final Summary")
    for result in results:
        print(
            f"{result['ai_name']}: "
            f"brand_mentioned={result['brand_mentioned']}, "
            f"rank={result['rank']}, "
            f"accuracy={result['accuracy_status']}"
        )


if __name__ == "__main__":
    main()
