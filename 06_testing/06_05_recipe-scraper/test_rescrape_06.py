# Write a unittest test suite to test the rescrape module

import unittest
import rescrape
from bs4 import BeautifulSoup

class TestRescrape(unittest.TestCase):

    def setUp(self):
        self.url = "https://codingnomads.github.io/recipes/"
        self.html = rescrape.get_page_content(self.url).text
        self.soup = BeautifulSoup(self.html, "html.parser")
        index_html = rescrape.get_html_content(self.url)
        index_soup = rescrape.make_soup(index_html)
        self.recipe_links = rescrape.get_recipe_links(index_soup)

    def test_get_page_content(self):
        page = rescrape.get_page_content(self.url)
        self.assertEqual(page.status_code, 200)

    def test_get_html_content(self):
        html = rescrape.get_page_content(self.url).text
        self.assertEqual(rescrape.get_page_content(self.url).text, html)

    def test_make_soup(self):
        self.assertEqual(rescrape.make_soup(self.html), self.soup)

    def test_get_recipe_links(self):
        links = [link["href"] for link in self.soup.find_all("a")]
        self.assertEqual(rescrape.get_recipe_links(self.soup), links)

    def test_get_author(self):
        for r_link in self.recipe_links:
            URL = f"{self.url}/{r_link}"
            soup = rescrape.make_soup(rescrape.get_html_content(URL))
        author = soup.find("p", class_="author").text.strip("by ")
        self.assertEqual(rescrape.get_author(soup), author)

    def test_get_recipe(self):
        for r_link in self.recipe_links:
            URL = f"{self.url}/{r_link}"
            soup = rescrape.make_soup(rescrape.get_html_content(URL))
        recipe = soup.find("div", class_="md").text
        self.assertEqual(rescrape.get_recipe(soup), recipe)


if __name__ == "__main__":
    unittest.main() 