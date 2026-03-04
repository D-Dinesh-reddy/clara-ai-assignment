# Clara AI Automation Pipeline

This project implements an automated pipeline that converts service business call transcripts into a structured **AI voice agent configuration**.

The goal is to simulate the onboarding workflow used by Clara AI to configure Retell voice agents for service businesses such as fire protection, HVAC, and electrical companies.

---

# System Architecture

The system processes two types of inputs:

1. **Demo Call Transcript**
2. **Onboarding Call Transcript**

These are converted into structured configuration files for an AI voice agent.

Pipeline overview:

Demo Call Transcript  
↓  
extract_data.py  
↓  
Account Memo JSON (v1)  
↓  
generate_agent.py  
↓  
Retell Agent Spec (v1)  
↓  
Onboarding Call Transcript  
↓  
update_agent.py  
↓  
Account Memo JSON (v2)  
↓  
Changelog Generation  

---

# Project Structure
