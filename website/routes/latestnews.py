import requests
from flask import Blueprint, render_template

latestnews = Blueprint('latestnews', __name__)

@latestnews.route('/latestnews')
def latest_news_page():
    API_KEY = 'f200ea7e949046c8aa4e2f63b6bf0ce0'  # Move this to .env later for safety
    url = (
        "https://newsapi.org/v2/everything?"
        "q=finance OR 'chartered accountant' OR 'government scheme' OR gst OR budget OR 'income tax'"
        "&language=en"
        "&sortBy=publishedAt"
        "&pageSize=5"
        "&domains=economictimes.indiatimes.com,business-standard.com,livemint.com,financialexpress.com,moneycontrol.com"
        f"&apiKey={API_KEY}"
    )

    try:
        response = requests.get(url)
        data = response.json()
        articles = data.get("articles", [])
    except Exception as e:
        print("Error fetching news:", e)
        articles = []

    return render_template('latestnews.html', news_items=articles)
