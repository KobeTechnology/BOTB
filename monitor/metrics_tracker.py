def calculate_metrics(results):
    """
    Calculates monitoring metrics from AI results.
    """

    total_ai_checked = len(results)

    brand_mentions = sum(1 for r in results if r["brand_mentioned"])
    hallucinations = sum(
        1 for r in results if r["accuracy_status"] == "Hallucination Detected"
    )

    brand_mention_rate = (
        round((brand_mentions / total_ai_checked) * 100, 2)
        if total_ai_checked
        else 0
    )

    hallucination_rate = (
        round((hallucinations / total_ai_checked) * 100, 2)
        if total_ai_checked
        else 0
    )

    return {
        "total_ai_checked": total_ai_checked,
        "brand_mention_rate": brand_mention_rate,
        "hallucination_rate": hallucination_rate
    }


if __name__ == "__main__":
    sample_results = [
        {"brand_mentioned": True, "accuracy_status": "Correct"},
        {"brand_mentioned": False, "accuracy_status": "N/A"},
        {"brand_mentioned": True, "accuracy_status": "Hallucination Detected"}
    ]

    print(calculate_metrics(sample_results))
