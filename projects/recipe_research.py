# Use your `Ingredients` class to create a URL to an online search
# that allows to look for recipes for dishes made from the
# available ingredients.

import webbrowser
from urllib.parse import quote

class Ingredient:
    """Models a food ingredient with a name and amount"""

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __str__(self):
        return f"{self.name}, {self.amount}"
    
    def search_recipe(self):
        """Opens a Google search for recipes using this ingredient"""
        query = f"recipes with {self.name}"
        encoded_query = quote(query)
        url = f"https://www.google.com/search?q={encoded_query}"
        print(f"Searching for recipes with {self.name}...")
        webbrowser.open(url)

# Interactive part
if __name__ == "__main__":
    user_input = input("Enter the name of an ingredient: ")
    ingredient = Ingredient(user_input, 1)
    ingredient.search_recipe()
