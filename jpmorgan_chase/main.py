import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('dataset.csv')

# Basic exploration
print("Dataset Info:")
print(df.info())        # Display data types and non-null counts
print("\nStatistical Summary:")
print(df.describe())    # Summary statistics for numerical columns

# Query 1: Transaction Type Distribution
print("\nTransaction Type Distribution:")
transaction_counts = df['type'].value_counts()  # Correct column name is 'type'
print(transaction_counts)

# Query 2: Fraud Analysis
flagged_fraud = df['isFlaggedFraud'].sum()
actual_fraud = df['isFraud'].sum()

print(f"\nFlagged fraud transactions: {flagged_fraud}")
print(f"Actual fraud transactions: {actual_fraud}")

# Query 3: Total Transaction Volume by Type
print("\nTransaction Volume by Type:")
volume_by_type = df.groupby('type')['amount'].sum()  # Correct column name is 'type'
print(volume_by_type)

# Stage 4: Visualizing the Data

# Visualize Transaction Type Distribution
plt.figure(figsize=(10, 6))
sns.countplot(x='type', data=df)  # Corrected column name to 'type'
plt.title('Transaction Type Distribution')
plt.xlabel('Transaction Type')
plt.ylabel('Count')
plt.show()

# Visualize Fraud Detection (Flagged vs Actual Fraud)
plt.figure(figsize=(6, 4))
fraud_counts = [flagged_fraud, actual_fraud]
fraud_labels = ['Flagged Fraud', 'Actual Fraud']
plt.bar(fraud_labels, fraud_counts, color=['blue', 'red'])
plt.title('Flagged vs Actual Fraud')
plt.ylabel('Number of Transactions')
plt.show()

# Visualize Transaction Volume by Type
plt.figure(figsize=(8, 6))
volume_by_type.plot(kind='bar')
plt.title('Transaction Volume by Type')
plt.ylabel('Total Volume')
plt.xlabel('Transaction Type')
plt.xticks(rotation=45)
plt.show()
