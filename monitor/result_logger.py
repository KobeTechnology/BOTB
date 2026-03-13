import json
from datetime import datetime
from pathlib import Path


LOG_FILE = Path("logs/monitoring_results.json")


def log_results(company_profile, results, metrics):
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "company": company_profile["company"],
        "product": company_profile["product"],
        "category": company_profile["category"],
        "results": results,
        "metrics": metrics
    }

    if not LOG_FILE.exists():
        LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
        LOG_FILE.write_text("[]")

    with open(LOG_FILE, "r") as file:
        existing_logs = json.load(file)

    existing_logs.append(log_entry)

    with open(LOG_FILE, "w") as file:
        json.dump(existing_logs, file, indent=4)

    print(f"Results logged for {company_profile['company']}.")
