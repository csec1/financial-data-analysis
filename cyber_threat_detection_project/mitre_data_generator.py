import random
import pandas as pd
from faker import Faker
import numpy as np

# Initialize Faker for random data generation
fake = Faker()

# MITRE ATT&CK Tactics (top-level categories of attack objectives)
tactics = [
    "Initial Access", "Execution", "Persistence", "Privilege Escalation", 
    "Defense Evasion", "Credential Access", "Discovery", "Lateral Movement", 
    "Collection", "Exfiltration", "Impact"
]

# MITRE ATT&CK Techniques (specific methods used by attackers)
techniques = [
    "Phishing", "Spearphishing Attachment", "Command and Scripting Interpreter", "PowerShell",
    "Exploitation of Vulnerability", "Taint Shared Content", "Access Token Manipulation", 
    "Credential Dumping", "Network Sniffing", "Ransomware", "Data Encrypted"
]

# Generate 1000 rows of synthetic data
data = []
for _ in range(1000):
    record = {
        "timestamp": fake.date_time_this_decade(),
        "attacker_name": fake.name(),
        "tactic": random.choice(tactics),
        "technique": random.choice(techniques),
        "attack_vector": random.choice(["Network", "Phishing", "USB", "Web", "Email"]),
        "severity": random.choice(["Low", "Medium", "High", "Critical"]),
        "affected_system": fake.word(),
        "ip_address": fake.ipv4(),
        "user_account": fake.user_name(),
        "region": random.choice(["US", "Europe", "Asia", "Africa", "South America", "Australia"]),
        "status": random.choice(["Successful", "Failed"]),
    }
    data.append(record)

# Create DataFrame from the data
mitre_df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
mitre_df.to_csv("data/mitre_attack_data.csv", index=False)

print("MITRE Attack data generated and saved as mitre_attack_data.csv")
