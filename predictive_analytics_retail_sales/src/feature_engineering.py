import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def create_features(data):
    """Create additional features for the model."""
    # Convert the 'date' column to datetime if it is not already
    if not pd.api.types.is_datetime64_any_dtype(data['date']):
        data['date'] = pd.to_datetime(data['date'])
    
    # Extract features
    data['year'] = data['date'].dt.year
    data['month'] = data['date'].dt.month
    data['day'] = data['date'].dt.day
    data['day_of_week'] = data['date'].dt.dayofweek
    return data

if __name__ == "__main__":
    # Get the paths from environment variables
    cleaned_data_path = os.getenv('CLEANED_DATA_PATH')
    feature_data_path = os.getenv('FEATURE_DATA_PATH')

    # Load the cleaned data
    #print(f"Loading cleaned data from: {cleaned_data_path}")
    cleaned_data = pd.read_csv(cleaned_data_path)
    print("Cleaned data loaded successfully.")
    
    # Create features
    print("Creating features...")
    feature_data = create_features(cleaned_data)
    print("Features created successfully.")
    
    # Save the feature data to a new CSV file
    feature_data.to_csv(feature_data_path, index=False)
    #print(f"Feature data saved to: {feature_data_path}")
