import pandas as pd
import os
from dotenv import load_dotenv

def load_data(filepath):
    """Load sales data from CSV file."""
    data = pd.read_csv(filepath)  # Use the provided filepath to load the CSV file
    #print(f"Data loaded successfully from {filepath}.")
    return data

def clean_data(data):
    """Placeholder for data cleaning logic."""
    # Implement any data cleaning steps here
    print("Data cleaned successfully.")
    return data

if __name__ == "__main__":
    # Load environment variables from .env file
    load_dotenv()
    
    # Access the file paths from the environment variables
    filepath = os.getenv('SALES_DATA_PATH')
    cleaned_data_path = os.getenv('CLEANED_DATA_PATH')

    # Load and clean the data
    sales_data = load_data(filepath)
    cleaned_data = clean_data(sales_data)
    
    # Save the cleaned data to a new CSV file
    cleaned_data.to_csv(cleaned_data_path, index=False)
    #print(f"Cleaned data saved to: {cleaned_data_path}")
