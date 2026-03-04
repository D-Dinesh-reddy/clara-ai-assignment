import subprocess

print("Running Demo Pipeline...")

subprocess.run(["py", "extract_data.py"])
subprocess.run(["py", "generate_agent.py"])

print("Running Onboarding Update...")

subprocess.run(["py", "update_agent.py"])

print("All pipelines executed successfully.")