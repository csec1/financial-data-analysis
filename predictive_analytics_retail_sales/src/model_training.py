import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import OneHotEncoder
import os
from dotenv import load_dotenv
import joblib  # Import joblib to save the model and encoder

# Load environment variables from .env file
load_dotenv()

def train_model(data: pd.DataFrame) -> RandomForestRegressor:
    """Train a Random Forest model on the sales data."""
    # Print the data types of each column
    print("Data Types Before Encoding:")
    print(data.dtypes)

    # Identify categorical columns
    categorical_cols = data.select_dtypes(include=['object']).columns.tolist()
    print("Categorical Columns:", categorical_cols)

    # Check for unique values in categorical columns
    for col in categorical_cols:
        print(f"Unique values in '{col}':", data[col].unique())

    # Initialize the encoder
    encoder = OneHotEncoder(drop='first', sparse_output=False)

    # Fit and transform the encoder on the categorical columns
    data_encoded = encoder.fit_transform(data[categorical_cols])
    data_encoded = pd.DataFrame(data_encoded, columns=encoder.get_feature_names_out(categorical_cols))
    
    # Concatenate encoded features with the original data (excluding categorical columns)
    data_encoded = pd.concat([data.drop(categorical_cols, axis=1).reset_index(drop=True), data_encoded.reset_index(drop=True)], axis=1)

    # Separate features and target variable
    X = data_encoded.drop(['sales'], axis=1)  # Drop only the target variable
    y = data_encoded['sales']  # Target variable

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create and train the model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Make predictions and evaluate the model
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    
    print(f'Model MSE: {mse}')

    # Save the encoder to the 'encoder/' directory
    encoder_path = os.path.join('encoder', 'encoder.joblib')  # Specify path for the encoder
    joblib.dump(encoder, encoder_path)  # Save encoder to specified path
    print(f'Encoder saved to: {encoder_path}')  # Confirmation message
    
    # Save the model to the 'model/' directory
    model_path = os.path.join('model', 'model.joblib')  # Specify path for the model
    joblib.dump(model, model_path)  # Save the model to specified path
    print(f'Model saved to: {model_path}')  # Confirmation message
    
    return model

if __name__ == "__main__":
    # Get the path from environment variable
    feature_data_path = os.getenv('FEATURE_DATA_PATH')
    
    # Load the feature data
    feature_data = pd.read_csv(feature_data_path)

    # Create necessary directories if they don't exist
    os.makedirs('encoder', exist_ok=True)  # Create encoder directory if it doesn't exist
    os.makedirs('model', exist_ok=True)    # Create model directory if it doesn't exist

    model = train_model(feature_data)
