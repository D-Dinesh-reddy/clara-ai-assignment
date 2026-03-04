import json
import os
from deepdiff import DeepDiff


def update_account(account_id):

    v1_path = f"../outputs/accounts/{account_id}/v1/memo.json"
    v2_folder = f"../outputs/accounts/{account_id}/v2"

    with open(v1_path) as f:
        v1_data = json.load(f)

    v2_data = v1_data.copy()

    # Simulate onboarding updates
    v2_data["business_hours"]["start"] = "08:00"
    v2_data["business_hours"]["end"] = "18:00"
    v2_data["office_address"] = "245 Main Street Dallas Texas"

    os.makedirs(v2_folder, exist_ok=True)

    v2_path = f"{v2_folder}/memo.json"

    with open(v2_path, "w") as f:
        json.dump(v2_data, f, indent=4)

    diff = DeepDiff(v1_data, v2_data)

    with open(f"../changelog/{account_id}_changes.json", "w") as f:
        json.dump(diff, f, indent=4)

    print("v2 memo created")
    print("Changelog generated")


if __name__ == "__main__":
    update_account("account_001")