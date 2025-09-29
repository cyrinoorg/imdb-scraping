import requests
from bs4 import BeautifulSoup

def scrape_imdb(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Add scraping logic here
    return soup.title.text

if __name__ == "__main__":
    print(scrape_imdb('https://www.imdb.com'))