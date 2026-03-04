# Clara AI Automation Pipeline

## Overview

This project implements an automated pipeline that converts service business call transcripts into a structured AI voice agent configuration.

The workflow simulates the onboarding process used by Clara Answers, where information from customer calls is transformed into operational rules and used to configure an AI voice receptionist.

The pipeline processes two stages:

1. Demo Call → Preliminary Agent (v1)
2. Onboarding Call → Updated Agent (v2)

The system automatically extracts operational information from transcripts, generates an agent configuration, and tracks version changes.

---

# Architecture and Data Flow

The automation pipeline converts conversational input into structured configuration files.

Pipeline A — Demo Call → Agent v1

Demo Call Transcript  
↓  
extract_data.py  
↓  
Account Memo JSON (v1)  
↓  
generate_agent.py  
↓  
Retell Agent Specification (v1)

---

Pipeline B — Onboarding Update → Agent v2

Onboarding Call Transcript  
↓  
update_agent.py  
↓  
Updated Account Memo JSON (v2)  
↓  
Regenerated Agent Configuration  
↓  
Changelog Generation  

This design ensures:

- clean separation between demo assumptions and onboarding confirmations
- version-controlled updates
- reproducible automation

---

# Repository Structure

clara-ai-assignment
│
├── workflows
│   └── pipeline_workflow.json
│
├── scripts
│   ├── extract_data.py
│   ├── generate_agent.py
│   ├── update_agent.py
│   ├── process_all.py
│   └── schema.py
│
├── transcripts
│   ├── demo_call_1.txt
│   └── onboarding_call_1.txt
│
├── outputs
│   └── accounts
│       └── account_001
│           ├── v1
│           │   ├── memo.json
│           │   └── agent.yaml
│           │
│           └── v2
│               └── memo.json
│
├── changelog
│   └── account_001_changes.json
│
└── README.md

---

# Account Memo JSON

The extracted account memo contains structured operational data including:

- account_id
- company_name
- business_hours
- office_address
- services_supported
- emergency_definition
- emergency_routing_rules
- non_emergency_routing_rules
- call_transfer_rules
- integration_constraints
- after_hours_flow_summary
- office_hours_flow_summary
- questions_or_unknowns
- notes

This structured memo becomes the source of truth for agent configuration.

---

# Retell Agent Draft Specification

The generated agent configuration includes:

- agent_name
- voice_style
- version
- key variables (business hours, address)
- call_transfer_protocol
- fallback_protocol
- system_prompt

The system prompt defines two operational flows.

Business Hours Flow

- greet caller
- ask purpose
- collect name and phone number
- route or transfer call
- fallback if transfer fails
- ask if caller needs anything else
- close the call

After Hours Flow

- greet caller
- confirm emergency status
- collect caller details
- attempt emergency transfer
- fallback if transfer fails
- assure follow-up
- close the call

---

# How to Run the Pipeline

Step 1 — Clone the Repository

git clone https://github.com/D-Dinesh-reddy/clara-ai-assignment  
cd clara-ai-assignment

---

Step 2 — Add Transcripts

Place transcript files in:

transcripts/

Example:

demo_call_1.txt  
onboarding_call_1.txt

---

Step 3 — Run the Automation Pipeline

cd scripts  
py process_all.py

This executes:

extract_data.py  
generate_agent.py  
update_agent.py  

---

# Output Files

Generated outputs are stored in:

outputs/accounts/<account_id>/

Example:

outputs/accounts/account_001/v1  
outputs/accounts/account_001/v2  

Artifacts include:

memo.json  
agent.yaml  

---

# Changelog

Changes between v1 and v2 are stored in:

changelog/account_001_changes.json

This file tracks:

- modified fields
- onboarding updates
- operational changes

---

# Workflow Export

The folder /workflows contains a pipeline export describing the automation steps used in this project.

This file demonstrates how the pipeline would be orchestrated in a workflow tool such as n8n.

---

# Retell Integration

This project generates a Retell Agent Specification compatible with the Retell platform.

If Retell API access is not available, the configuration can be manually applied by:

1. Creating a new agent in the Retell dashboard
2. Copying the generated system_prompt
3. Setting variables and routing rules based on the generated YAML

---

# Limitations

- Extraction logic is rule-based rather than LLM-based
- Designed for transcript input rather than audio processing
- Only a small sample dataset is included
- Some routing rules may remain under questions_or_unknowns if missing

---

# Future Improvements

With production access, the system could be extended to include:

- automated speech-to-text transcription
- LLM-based extraction for higher accuracy
- integration with CRM systems such as ServiceTrade
- a web dashboard for reviewing agent versions
- automated workflow orchestration via n8n

---

# Summary

This project demonstrates an automated system that transforms unstructured customer conversations into version-controlled AI voice agent configurations.

The pipeline is:

- automated
- reproducible
- versioned
- zero-cost
- ready for expansion into production workflows.