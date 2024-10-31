import pandas as pd
import joblib
import os
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

def evaluate_model(model, data: pd.DataFrame, encoder):
    """Evaluate the Random Forest model on the given data."""
    # Perform one-hot encoding using the loaded encoder
    data_encoded = encoder.transform(data.select_dtypes(include=['object']))

    # Combine encoded data with numerical features
    numeric_data = data.select_dtypes(exclude=['object'])
    data_encoded_df = pd.DataFrame(data_encoded, columns=encoder.get_feature_names_out())
    data_final = pd.concat([numeric_data.reset_index(drop=True), data_encoded_df.reset_index(drop=True)], axis=1)

    # Separate features and target variable
    X = data_final.drop(['sales'], axis=1)  # Drop only the target variable
    y = data_final['sales']  # Target variable

    # Make predictions
    predictions = model.predict(X)

    # Calculate evaluation metrics
    mse = mean_squared_error(y, predictions)
    
    print(f'Model MSE: {mse:.2f}')

    # Plotting the predictions vs actual values
    plt.figure(figsize=(10, 6))
    plt.scatter(y, predictions, alpha=0.6, label='Predicted vs Actual')
    plt.plot([y.min(), y.max()], [y.min(), y.max()], '--r', label='Perfect Prediction')
    plt.xlabel('Actual Sales')
    plt.ylabel('Predicted Sales')
    plt.title('Actual vs Predicted Sales')
    plt.legend()
    plt.grid()
    plt.show()

    # Print a sample of the actual and predicted sales
    results_df = pd.DataFrame({'Actual Sales': y, 'Predicted Sales': predictions})
    
    # Display the first few rows of the results
    print("\nSample of Actual vs Predicted Sales:")
    print(results_df.head(10))  # Change the number to display more or fewer rows

    # Describe the results
    print("\nSales Data Description:")
    print(results_df.describe())

if __name__ == "__main__":
    # Get paths from environment variables
    feature_data_path = os.getenv('FEATURE_DATA_PATH')
    model_path = os.getenv('MODEL_PATH')
    encoder_path = os.getenv('ENCODER_PATH')

    # Load the feature data
    feature_data = pd.read_csv(feature_data_path)

    # Load the trained model and encoder
    model = joblib.load(model_path)  # Load the trained model
    encoder = joblib.load(encoder_path)  # Load the trained encoder

    # Evaluate the model
    evaluate_model(model, feature_data, encoder)
