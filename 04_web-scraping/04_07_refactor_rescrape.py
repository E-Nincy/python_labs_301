# Refactor your web scraping script and wrap all the functionality into
# separate functions. This is a great exercise to revisit writing functions
# as well as for refactoring your code. It'll also help you in an upcoming
# section of the course when you'll write tests for your web scraper.

import requests
from bs4 import BeautifulSoup

def download_page(url, filename):
    """Download and save the HTML page locally."""
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(response.text)
        print(f"Page saved to {filename}")
    else:
        print(f"Failed to fetch page. Status: {response.status_code}")

def load_local_html(filename):
    """Load HTML content from a local file."""
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()

def parse_quotes(html):
    """Parse quotes and authors from HTML content."""
    soup = BeautifulSoup(html, "html.parser")
    quotes_data = []
    quotes = soup.find_all("div", class_="quote")
    for q in quotes:
        text = q.find("span", class_="text").get_text()
        author = q.find("small", class_="author").get_text()
        quotes_data.append((text, author))
    return quotes_data

def display_quotes(quotes):
    """Print quotes to the terminal."""
    for quote, author in quotes:
        print(f"{quote} — {author}")

def main():
    url = "https://quotes.toscrape.com"
    filename = "quotes.html"
    
    download_page(url, filename)
    html = load_local_html(filename)
    quotes = parse_quotes(html)
    display_quotes(quotes)

if __name__ == "__main__":
    main()
