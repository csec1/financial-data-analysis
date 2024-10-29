import requests
import os
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment(articles):
    analyzer = SentimentIntensityAnalyzer()
    for article in articles:
        title = article['title']
        sentiment = analyzer.polarity_scores(title)  # Analyze sentiment of the title
        
        # Categorize sentiment
        if sentiment['compound'] > 0.05:
            sentiment_label = "Positive"
        elif sentiment['compound'] < -0.05:
            sentiment_label = "Negative"
        else:
            sentiment_label = "Neutral"
        
        article['sentiment'] = {
            'score': sentiment,
            'label': sentiment_label  # Add the label to the article
        }
    return articles

def fetch_news():
    api_key = os.getenv('API_KEY')  # Load the API key from environment variables
    # Adjust pageSize to fetch more articles
    url = f'https://api.goperigon.com/v1/all?apiKey={api_key}&pageSize=20'  # Increase the number of articles

    response = requests.get(url)
    
    if response.status_code == 200:
        news_data = response.json()
        # Filter for English articles
        english_articles = [
            article for article in news_data['articles'] if article.get('language') == 'en'
        ]
        # Analyze sentiment of the articles
        articles_with_sentiment = analyze_sentiment(english_articles)
        return articles_with_sentiment  # Return articles with sentiment
    else:
        print(f"Error fetching news: {response.status_code}")
        return []
