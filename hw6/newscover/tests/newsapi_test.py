from datetime import date, timedelta, datetime
import unittest, json, os
import newsapi

def get_key():
        with open(os.path.join(os.path.dirname(__file__), "test_secrets.json"), "r") as f:
            data = json.load(f)
            return data["key"]
        
def convertDate(date):
     new_date = datetime.strptime(date,"%Y-%m-%dT%H:%M:%SZ")
     return new_date.date()

class NewsAPITestCase(unittest.TestCase):

    def test_no_keywords(self):
        with self.assertRaises(ValueError):
            newsapi.fetch_latest_news(api_key=get_key())

    def test_alphabetic(self):
        with self.assertRaises(ValueError):
            newsapi.fetch_latest_news(get_key(), "test", "test1")

    def test_lookback_days(self):
        days = 2

        news = newsapi.fetch_latest_news(get_key(), "trump", "trial", lookback_days=days)
        dates = [convertDate(article["publishedAt"]) for article in news["articles"]]
        oldest_date = date.today() - timedelta(days=days)

        valid_date = [(date >= oldest_date) for date in dates]
        self.assertTrue(all(valid_date))
        
if __name__ == "__main__":
    unittest.main()