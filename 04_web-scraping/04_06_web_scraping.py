# Look for a static website online that has some information that you're
# interested in. Follow the web-scraping steps described in the course to
# inspect, scrape, and parse the information.
# BE RESPECTFUL! Don't scrape sites that don't want to be scraped, and
# limit the amount of calls you make to their page by saving the response
# to a file, and parsing the content from that file.

import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com"

# Download the page and save it locally (just once)
response = requests.get(url)
with open("quotes.html", "w", encoding="utf-8") as file:
    file.write(response.text)

# Parse the saved HTML file
with open("quotes.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# Extract quotes and authors
quotes = soup.find_all("div", class_="quote")

for q in quotes:
    text = q.find("span", class_="text").get_text()
    author = q.find("small", class_="author").get_text()
    print(f"{text} — {author}")
