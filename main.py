
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    """
    Main page displaying recent news articles.
    """
    news_articles = get_news_articles()
    return render_template('index.html', articles=news_articles)

@app.route('/refresh_news')
def refresh_news():
    """
    Refreshes the list of news articles.
    """
    news_articles = get_news_articles()
    return render_template('index.html', articles=news_articles)

def get_news_articles():
    """
    Fetches the latest news articles from an API or database.
    """
    # Replace this with actual implementation to fetch news articles
    return [
        {'title': 'Sample Article 1', 'author': 'Author 1', 'time': '1 hour ago'},
        {'title': 'Sample Article 2', 'author': 'Author 2', 'time': '2 hours ago'},
    ]

if __name__ == "__main__":
    app.run(debug=True)
