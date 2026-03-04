import json
import yaml
import os

def generate_agent(account_id):

    memo_path = f"../outputs/accounts/{account_id}/v1/memo.json"

    with open(memo_path) as f:
        memo = json.load(f)

    agent_config = {
        "agent_name": f"{memo['company_name']} Assistant",
        "voice_style": "professional",
        "version": "v1",
        "variables": {
            "business_hours": memo["business_hours"],
            "office_address": memo["office_address"]
        },
        "system_prompt": f"""
You are a professional AI receptionist for {memo['company_name']}.

BUSINESS HOURS FLOW:
- Greet the caller politely
- Ask for the purpose of the call
- Collect caller name and phone number
- Route the call if needed
- If transfer fails, collect message and assure follow-up
- Ask if they need anything else
- Close politely

AFTER HOURS FLOW:
- Greet caller
- Ask reason for call
- Check if it is an emergency
- If emergency: collect name, phone, and address immediately
- Attempt transfer to emergency contact
- If transfer fails: assure fast follow-up
- If non-emergency: collect request and schedule follow-up
- Close politely
"""
    }

    output_folder = f"../outputs/accounts/{account_id}/v1"
    os.makedirs(output_folder, exist_ok=True)

    output_file = f"{output_folder}/agent.yaml"

    with open(output_file, "w") as f:
        yaml.dump(agent_config, f)

    print("Agent config created at:", output_file)


if __name__ == "__main__":
    generate_agent("account_001")