# 1. **Libraries and Installations**
import requests
import pandas as pd
import nltk
import spacy
import random
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
from transformers import pipeline
from flask import Flask, request, jsonify
import pickle
from flask_cors import CORS  # New import for CORS support

#/////////////////////////////////////////////////////////
# 2. **Read the Generated Customer Comments from CSV**
# Load the customer feedback dataset from the generated CSV
data_loaded = False
try:
    df = pd.read_csv("customer_feedback.csv")
    if not df.empty:
        print(f"Loaded {len(df)} comments from 'customer_feedback.csv'")
        print(df.head())
        data_loaded = True
    else:
        print("No data available.")
except FileNotFoundError:
    print("The file 'customer_feedback.csv' was not found.")

#/////////////////////////////////////////////////////////
# 3. **Data Preprocessing (ETL)**

# Check if NLTK datasets are already downloaded
nltk_data_installed = True
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk_data_installed = False

if not nltk_data_installed:
    print("Downloading NLTK datasets...")
    nltk.download('punkt')
    nltk.download('stopwords')
else:
    print("NLTK datasets are already installed.")

# Text Preprocessing Function
def preprocess_text(text):
    # Lowercase
    text = text.lower()
    
    # Tokenization
    tokens = word_tokenize(text)
    
    # Remove punctuation and stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words and word not in string.punctuation]
    
    return " ".join(tokens)

# Apply preprocessing to customer feedback column if data is loaded
if data_loaded:
    df['cleaned_feedback'] = df['feedback'].apply(preprocess_text)

#/////////////////////////////////////////////////////////
# 4. **Sentiment Analysis Using LLM (Replaced VADER with LLM)**

# Specify the pre-trained LLM model (DistilBERT)
sentiment_model = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Example using LLM to analyze sentiment of a feedback
def analyze_sentiment_with_llm(feedback):
    result = sentiment_model(feedback)
    return result

# Apply LLM sentiment analysis to the cleaned feedback
if data_loaded:
    df['llm_sentiment'] = df['cleaned_feedback'].apply(analyze_sentiment_with_llm)

# Display the updated dataframe with LLM sentiment
if data_loaded:
    print(df[['feedback', 'llm_sentiment']].head())

#/////////////////////////////////////////////////////////
# 5. **Model Training and Evaluation**

# Preprocess data for training (you can use cleaned feedback for this)
if data_loaded:
    X_train, X_test, y_train, y_test = train_test_split(df['cleaned_feedback'], df['llm_sentiment'].apply(lambda x: x[0]['label']), test_size=0.3, random_state=42)

    # Vectorize the text data using TF-IDF
    vectorizer = TfidfVectorizer(max_features=1000)
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)

    # Train a Naive Bayes model (or any other classifier)
    model = MultinomialNB()
    model.fit(X_train_tfidf, y_train)

    # Evaluate the model on the test set
    y_pred = model.predict(X_test_tfidf)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))

    # Save the trained model and vectorizer (for later use in the Flask app)
    with open('sentiment_model.pkl', 'wb') as f:
        pickle.dump(model, f)

    with open('vectorizer.pkl', 'wb') as f:
        pickle.dump(vectorizer, f)

#/////////////////////////////////////////////////////////
# 6. **Create an API to Serve the Model**

# Initialize Flask app
app = Flask(__name__)

# Enable CORS for all routes (important if front-end and back-end are on different ports)
CORS(app)  # Allows cross-origin requests

# Preprocess text for prediction
def preprocess_input(text):
    return preprocess_text(text)

# Load trained model and vectorizer
with open('sentiment_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Define the predict route for API
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return jsonify({"message": "This endpoint only accepts POST requests."})

    
    
    if request.method == 'POST':
        # Extract feedback text from the request
        feedback = request.json['feedback']
        
        # Preprocess the feedback
        processed_feedback = preprocess_input(feedback)
        
        # Transform using vectorizer
        feedback_tfidf = vectorizer.transform([processed_feedback])
        
        # Make prediction
        prediction = model.predict(feedback_tfidf)
        
        # Return response
        return jsonify({'sentiment': prediction[0]})

# Serve static HTML page (index.html) as a front-end interface
@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)
