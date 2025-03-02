### Sentiment Analysis Project

This project uses **Flask** for serving a sentiment analysis model via an API and provides a simple front-end interface for user interaction. The sentiment analysis is powered by a **Naive Bayes classifier** trained on customer feedback data. The following tools and files are involved:

1. **Tools & Libraries**:
   - **Flask**: To build the backend API.
   - **NLTK, SpaCy**: For text preprocessing and stopword removal.
   - **scikit-learn**: For model training (Naive Bayes) and TF-IDF vectorization.
   - **transformers (DistilBERT)**: For sentiment analysis using pre-trained models.
   - **Pickle**: To save and load the trained model and vectorizer.

2. **Files**:
   - **index.html**: The front-end page that collects feedback and displays sentiment results. It communicates with the Flask API using POST requests.
   - **main.rev5.py**: The Python file that handles data loading, preprocessing, model training, API creation (using Flask), and serves the model through the `/predict` endpoint.

3. **Data**:
   - The customer feedback data (`customer_feedback.csv`) is loaded, cleaned, and used for model training. Sentiment is predicted for each feedback, which is then served via the Flask API.

The project includes proper handling of **CORS** to enable smooth communication between front-end and back-end when hosted on different ports.

Few Runtime backend and frontend pictures supplied in this directory, keep in mind that the jupyter notebook added here complains of teh non-production set up but the actual production environment was run via gunicorn which is being shown in a linux pic in this directory.