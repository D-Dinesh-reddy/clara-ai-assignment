import json
import os
from extract_data import extract_information


def load_json(path):
    with open(path, "r") as f:
        return json.load(f)


def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)


def update_account(account_id):

    v1_path = f"../outputs/accounts/{account_id}/v1/memo.json"
    transcript_path = "../transcripts/onboarding_call_1.txt"

    v1_data = load_json(v1_path)

    with open(transcript_path, "r") as f:
        transcript = f.read()

    extracted_update = extract_information(transcript)

    updated_data = v1_data.copy()
    changelog = {}

    for key in v1_data:

        old_value = v1_data[key]
        new_value = extracted_update.get(key)

        # Skip account_id
        if key == "account_id":
            continue

        # Only update if new value is meaningful
        if new_value and new_value != old_value:

            updated_data[key] = new_value

            changelog[key] = {
                "old": old_value,
                "new": new_value
            }

    v2_folder = f"../outputs/accounts/{account_id}/v2"
    os.makedirs(v2_folder, exist_ok=True)

    v2_path = f"{v2_folder}/memo.json"
    save_json(v2_path, updated_data)

    changelog_path = f"../changelog/{account_id}_changes.json"
    save_json(changelog_path, changelog)

    print("v2 memo created")
    print("Changelog generated")


if __name__ == "__main__":

    update_account("account_001")