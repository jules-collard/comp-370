import unittest, json, os
import newsapi

def get_key():
        with open(os.path.join(os.path.dirname(__file__), "test_secrets.json"), "r") as f:
            data = json.load(f)
            return data["key"]

class NewsAPITestCase(unittest.TestCase):

    def test_no_keywords(self):
        with self.assertRaises(ValueError):
            newsapi.fetch_latest_news(api_key=get_key())

    def test_alphabetic(self):
        with self.assertRaises(ValueError):
            newsapi.fetch_latest_news(get_key(), "test", "test1")
        
if __name__ == "__main__":
    unittest.main()