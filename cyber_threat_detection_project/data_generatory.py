from faker import Faker
import pandas as pd

# Initialize Faker instance
fake = Faker()

# List of MITRE ATT&CK techniques (sample subset for demonstration)
techniques = [
    "Spearphishing Attachment", 
    "Spearphishing Link", 
    "Sudo Caching", 
    "Scheduled Task", 
    "Data Staged", 
    "Brute Force", 
    "Application Layer Protocol",
    "Remote File Copy",
    "Command and Control Over Web Protocol"
]

# Define the number of records
num_records = 1000

# Create an empty list to store the generated data
data = []

# Generate data
for _ in range(num_records):
    data.append({
        "timestamp": fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S"),
        "attacker_name": fake.name(),
        "tactic": fake.word().capitalize(),
        "technique": fake.random_element(techniques),
        "attack_vector": fake.word().capitalize(),
        "severity": fake.random_element(["Low", "Medium", "High"]),
        "affected_system": fake.word(),
        "ip_address": fake.ipv4(),
        "user_account": fake.user_name(),
        "region": fake.random_element(["Europe", "Asia", "North America", "South America"]),
        "status": fake.random_element(["Failed", "Successful"]),
        "severity_num": fake.random_int(min=1, max=3),
        "attack_vector_num": fake.random_int(min=1, max=4),
        "region_num": fake.random_int(min=1, max=4),
        "hour": fake.random_int(min=0, max=23),
        "day": fake.random_int(min=1, max=31),
        "month": fake.random_int(min=1, max=12),
        "anomaly": fake.boolean()
    })

# Convert the list of data to a DataFrame
df = pd.DataFrame(data)

# Save the data to a CSV file
df.to_csv("mitre_cyber_threats.csv", index=False)

# Show first 5 rows of the generated data
print(df.head())
