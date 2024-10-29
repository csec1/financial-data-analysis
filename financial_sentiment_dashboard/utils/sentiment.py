from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment(articles):
    analyzer = SentimentIntensityAnalyzer()
    for article in articles:
        title = article['title']
        sentiment = analyzer.polarity_scores(title)  # Analyze sentiment of the title
        article['sentiment'] = sentiment  # Add sentiment scores to the article
    return articles
