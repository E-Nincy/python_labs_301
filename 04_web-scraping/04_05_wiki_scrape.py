# Write a web scraper that fetches the information from the Wikipedia page
# on Web scraping. Extract all the links on the page and filter them so the
# navigation links are excluded.
# Programmatically follow one of the links that lead to another Wikipedia article,
# extract the text content from that article, and save it to a local text file.
# BONUS TASK: Use RegExp to find all numbers in the text.

URL = "https://en.wikipedia.org/wiki/Web_scraping"

import requests
from bs4 import BeautifulSoup
import re

url = "https://en.wikipedia.org/wiki/Web_scraping"
base = "https://en.wikipedia.org"

res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

# Get valid article links (not menus, not files)
links = [a["href"] for a in soup.select("a[href^='/wiki/']") 
         if not any(x in a["href"] for x in [":", "#", "Main_Page"])]
article_url = base + links[0]

# Get text from the linked article
article = BeautifulSoup(requests.get(article_url).text, "html.parser")
text = "\n".join(p.text for p in article.find_all("p"))

# Save to file
with open("article.txt", "w", encoding="utf-8") as f:
    f.write(text)

#Bonus task
numbers = re.findall(r'\d+', text)
print(f"Saved article. Found {len(numbers)} numbers: {numbers[:10]}")
