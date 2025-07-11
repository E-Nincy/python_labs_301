import unittest
import rescrape 

class TestRescrape(unittest.TestCase):
    
    # requests can esetablish a connection and receive a valid response
    def test_get_valid_html_response(self):
        BASE_URL = "https://codingnomads.github.io/recipes/"
        index_page = rescrape.get_page_content(BASE_URL)
        self.assertEqual(index_page.status_code, 200)

    # the response contains HTML code
    def test_response_contains_html(self):
        response = rescrape.get_page_content(rescrape.BASE_URL)
        self.assertIn("<html", response.text.lower())

    # the HTML can be successfully converted to a Beautiful Soup object
    def test_can_convert_to_soup(self):   
        soup = rescrape.get_soup_from_url(rescrape.BASE_URL)
        self.assertIsNotNone(soup.find("a"))

    # can identify all links from the index page
    def test_can_get_recipe_links(self):
        links = rescrape.get_recipe_links()
        self.assertTrue(len(links) > 0)
        self.assertTrue(all(link.endswith(".html") for link in links))

    # can identify the author of a recipe
    def test_can_get_author_from_recipe(self):
        links = rescrape.get_recipe_links()
        url = rescrape.BASE_URL + links [0]
        author, _ = rescrape.get_author_and_text(url)
        self.assertIsNotNone(author)

    # can get the main recipe text
    def test_can_get_main_recipe_text(self):
        links = rescrape.get_recipe_links()
        url = rescrape.BASE_URL + links[0]
        _, recipe_text = rescrape.get_author_and_text(url)
        self.assertIsNotNone(recipe_text)
        self.assertGreater(len(recipe_text), 30)


if __name__ == "__main__":
    unittest.main()

