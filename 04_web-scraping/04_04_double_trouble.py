# Research for interesting APIs online and pick two. You can also use APIs that
# you've already worked with in the course if you prefer.
# Write a program that makes calls to both APIs and find a way to combine the
# data that you receive from both of them.
# E.g.: You could use the Ghibli API to find all ghosts from their films, and
#       create an opposing team of Ghost Pokémon from the Poke API.

import requests

def get_ghibli_people():
    url = "https://ghibliapi.vercel.app/people"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error fetching Ghibli data")
        return []

    try:
        res = response.json()
        return [p["name"] for p in res]
    except Exception as e:
        print("Error parsing Ghibli JSON:", e)
        return []

def get_ghost_pokemon():
    url = "https://pokeapi.co/api/v2/type/ghost"
    res = requests.get(url).json()
    return [p["pokemon"]["name"].capitalize() for p in res["pokemon"]]

def main():
    people = get_ghibli_people()
    print("All Ghibli characters:")
    for name in people:
        print(f"- {name}")

    ghost_pokemon = get_ghost_pokemon()
    print("\nGhost Pokémon:")
    for p in ghost_pokemon:
        print(f"- {p}")

if __name__ == "__main__":
    main()
