from argparse import ArgumentParser
from newsapi import fetch_latest_news
import json, os

def main():
    parser = ArgumentParser(
        prog="Collector",
        description="Calls to News API and saves results as JSON files"
    )
    parser.add_argument("-k", "--key", help="API Key", required=True)
    parser.add_argument("-b", "--back", help="Number of days to look back", required=False, default=10)
    parser.add_argument("-i", "--input", help="Input JSON file", required=True)
    parser.add_argument("-o", "--output", help="Output Directory", required=True)

    args = parser.parse_args()

    with open(args.input, "r") as f:
        keyword_dict = json.load(f)
    
    for key, value in keyword_dict.items():
        news = fetch_latest_news(args.key, *value, lookback_days=args.back)
        filename = os.path.join(args.output, key + ".json")

        with open(filename, "w") as f:
            json.dump(news, f)

if __name__ == "__main__":
    main()