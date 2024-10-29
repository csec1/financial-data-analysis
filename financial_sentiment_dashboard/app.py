from flask import Flask, render_template
from scraping.scraper import fetch_news

app = Flask(__name__)

@app.route('/')
def index():
    articles = fetch_news()  # Fetch news articles using the API
    return render_template('index.html', articles=articles)

if __name__ == '__main__':
    app.run(debug=True)
