import argparse, bs4, requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def main():
    parser = argparse.ArgumentParser(
        prog="TrendingCollector",
        description="Collects trending articles from montrealgazette.com/category/news/"
    )
    parser.add_argument("-o", "--output", help="Output JSON file", required=True)
    parser.parse_args()


def get_trending(download=False, filename="frontpage.html"):
    
    # Download front page HTML content
    if download:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://montrealgazette.com/category/news/")
        
        with open(filename, "w") as f:
            f.write(driver.page_source)
        
        driver.quit()

    with open(filename, "r") as f:
        soup = bs4.BeautifulSoup(f, "html.parser")
    
    headlines = soup.find_all("h3", attrs={"class":"article-card_headline"})
    for h in headlines:
        print(h["href"])


if __name__ == "__main__":
    get_trending(download=True)
    

