import json
import os
from schema import ACCOUNT_SCHEMA


def extract_information(transcript_text):

    data = ACCOUNT_SCHEMA.copy()

    text = transcript_text.lower()
    lines = transcript_text.split("\n")

    # -----------------------------
    # Extract Company Name
    # -----------------------------
    for line in lines:
        if "company:" in line.lower():
            data["company_name"] = line.split(":", 1)[1].strip()

    # -----------------------------
    # Extract Office Address / Location
    # -----------------------------
    for line in lines:
        if "address:" in line.lower():
            data["office_address"] = line.split(":", 1)[1].strip()

        if "location:" in line.lower():
            data["office_address"] = line.split(":", 1)[1].strip()

    # -----------------------------
    # Extract Business Hours
    # -----------------------------
    if "monday to friday" in text:
        data["business_hours"]["days"] = ["Mon", "Tue", "Wed", "Thu", "Fri"]

    if "8:00" in text or "8am" in text:
        data["business_hours"]["start"] = "08:00"

    if "4:30" in text:
        data["business_hours"]["end"] = "16:30"

    if "5:00" in text:
        data["business_hours"]["end"] = "17:00"

    # -----------------------------
    # Extract Services
    # -----------------------------
    services = []

    if "electrical repair" in text:
        services.append("electrical repairs")

    if "commercial electrical" in text:
        services.append("commercial electrical work")

    if "troubleshooting" in text:
        services.append("electrical troubleshooting")

    if "ev charger" in text:
        services.append("EV charger installation")

    if "hot tub" in text:
        services.append("hot tub electrical hookup")

    if "panel upgrade" in text:
        services.append("panel upgrades")

    if "renovation" in text:
        services.append("electrical renovation work")

    data["services_supported"] = list(set(services))

    # -----------------------------
    # Extract Emergency Definitions
    # -----------------------------
    emergencies = []

    if "gas station" in text:
        emergencies.append("gas station electrical emergency")

    if "urgent repair" in text:
        emergencies.append("urgent electrical repair")

    data["emergency_definition"] = emergencies

    # -----------------------------
    # Detect Missing Information
    # -----------------------------
    if data["office_address"] == "":
        data["questions_or_unknowns"].append("office_address missing")

    if data["business_hours"]["start"] == "" or data["business_hours"]["end"] == "":
        data["questions_or_unknowns"].append("business_hours missing")

    data["notes"] = "Generated from transcript"

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