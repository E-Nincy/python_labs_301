# For this project, your task is to create a CLI that takes as an input
# the names of ingredients from a user. Then, your code will fetch
# the recipe information from the CodingNomads recipe collection,
# and search through the text of the recipes to find ones that include
# the provided ingredients.
#
# Note: Feel free to integrate your custom Ingredient() and Soup() classes
# into the code base, to get some additional practice in working with your
# custom Python classes.

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://codingnomads.github.io/recipes/"

def get_page_content(url):
    """Makes an HTTP request to the given URL and returns the response."""
    page = requests.get(url)
    return page

def get_recipe_links():
    """Gets all recipe links from the index page."""
    index_html = get_page_content(BASE_URL).text
    index_soup = BeautifulSoup(index_html, "html.parser")
    return [link["href"] for link in index_soup.find_all("a")]

def find_recipes_with_ingredients(ingredients):
    """Searches for recipes that contain all the given ingredients."""
    recipe_links = get_recipe_links()
    found_recipes = []

    for r_link in recipe_links:
        URL = f"{BASE_URL}/{r_link}"
        html = get_page_content(URL).text
        soup = BeautifulSoup(html, "html.parser")

        author_tag = soup.find("p", class_="author")
        recipe_tag = soup.find("div", class_="md")

        if author_tag and recipe_tag:
            author = author_tag.text.strip("by ")
            recipe_text = recipe_tag.text.lower()

            # Check if all ingredients are in the recipe
            if all(ing in recipe_text for ing in ingredients):
                found_recipes.append((author, recipe_text.strip(), r_link))

    return found_recipes

if __name__ == "__main__":
    print("Welcome to the CLI Recipe Finder!")

    # Ask user for ingredients
    user_input = input("Enter ingredients separated by commas: ")
    ingredients = [i.strip().lower() for i in user_input.split(",")]

    print(f"\nSearching for recipes with: {', '.join(ingredients)}\n")

    matching_recipes = find_recipes_with_ingredients(ingredients)

    if matching_recipes:
        for author, recipe, link in matching_recipes:
            print("Recipe found!")
            print(f"Author: {author}")
            print(f"Link: {BASE_URL}/{link}")
            print(f"Recipe preview:\n{recipe[:500]}...")  # Preview first 500 characters
            print("-" * 50)
    else:
        print("No recipes found with those ingredients.")



