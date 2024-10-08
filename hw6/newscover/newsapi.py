import requests, json
from datetime import date, timedelta

def fetch_latest_news(api_key, *news_keywords, lookback_days=10):
    url = "https://newsapi.org/v2/everything"
    oldest_date = date.today() - timedelta(days=lookback_days)
    
    if not news_keywords or not all([key.isalpha() for key in news_keywords]):
        raise ValueError
        return

    response = requests.get(url, params = {
        "apiKey": api_key,
        "q": ' AND '.join(news_keywords),
        "language": "en",
        "from": oldest_date
    })

    response.raise_for_status()
    data = response.json()
    return data