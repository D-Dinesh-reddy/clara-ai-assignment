import json
import os
from schema import ACCOUNT_SCHEMA


def extract_information(transcript_text):

    data = ACCOUNT_SCHEMA.copy()

    text = transcript_text.lower()

    # Extract company name (simple placeholder)
    if "company" in text:
        data["company_name"] = "Unknown Company"

    # Services
    if "sprinkler" in text:
        data["services_supported"].append("sprinkler services")

    if "fire alarm" in text:
        data["services_supported"].append("fire alarm systems")

    if "hvac" in text:
        data["services_supported"].append("HVAC service")

    # Emergency definitions
    if "leak" in text:
        data["emergency_definition"].append("sprinkler leak")

    if "alarm triggered" in text:
        data["emergency_definition"].append("fire alarm triggered")

    # Business hours detection (very simple rule)
    if "9 to 5" in text:
        data["business_hours"]["days"] = ["Mon","Tue","Wed","Thu","Fri"]
        data["business_hours"]["start"] = "09:00"
        data["business_hours"]["end"] = "17:00"

    # Missing info detection
    if "address" not in text:
        data["questions_or_unknowns"].append("office_address missing")

    if "business hours" not in text:
        data["questions_or_unknowns"].append("business_hours missing")

    data["notes"] = "Generated from demo transcript"

    return data


def process_transcript(file_path, account_id):

    with open(file_path, "r") as file:
        transcript = file.read()

    extracted = extract_information(transcript)

    extracted["account_id"] = account_id

    output_folder = f"../outputs/accounts/{account_id}/v1"
    os.makedirs(output_folder, exist_ok=True)

    output_file = f"{output_folder}/memo.json"

    with open(output_file, "w") as file:
        json.dump(extracted, file, indent=4)

    print("Account memo created at:", output_file)


if __name__ == "__main__":

    process_transcript(
        "../transcripts/demo_call_1.txt",
        "account_001"
    )