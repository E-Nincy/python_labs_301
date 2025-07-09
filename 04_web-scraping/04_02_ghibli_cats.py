# Read through the documentation of the Ghibli API and reproduce the example
# listed at https://ghibliapi-iansedano.vercel.app/#section/Use-Case in Python.
# Try skim the Haskell code example and see if you can understand anything.
# Don't worry if you don't, it's a completely different language :)
#
# Your task is to use the API to find information about all the cats that
# appear in Studio Ghibli films.

import requests
from pprint import pprint

BASE_URL = "https://ghibliapi-iansedano.vercel.app"

response = requests.get(f"{BASE_URL}/api/people")
people = response.json()

cat_characters = []

for person in people:
    if isinstance(person, dict):
        name = person.get("name", "").lower()
        species = person.get("species", "").lower()
        
        if "cat" in name or "cat" in species:
            cat_characters.append(person)

print("Studio Ghibli Cats:")
pprint(cat_characters)
