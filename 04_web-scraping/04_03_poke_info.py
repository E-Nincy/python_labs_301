# Use the Pokemon API at https://pokeapi.co/ to assemble a team of your
# six favorite Pokémon.
# Your task is to fetch information about six Pokémon through the
# necessary API calls and include the information in your local script.
# This information should include at least:
# - name
# - number
# - types
#
# You can improve on your project even more by writing the data to a small
# `.html` page which allows you to also display the sprites of each Pokémon.
# Check out the guides they provide: https://pokeapi-how.appspot.com/page5

import requests

BASE_URL = "https://pokeapi.co/api/v2/"

# Put my 6 favorite Pokémon here (names or IDs)
team = ["pikachu", "charizard", "mewtwo", "bulbasaur", "gengar", "lucario"]

def get_pokemon_data(name_or_id):
    url = f"{BASE_URL}pokemon/{name_or_id.lower()}"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error: Could not find {name_or_id}")
        return None
    data = response.json()
    pokemon_info = {
        "name": data["name"].capitalize(),
        "number": data["id"],
        "types": [t["type"]["name"].capitalize() for t in data["types"]],
        "sprite": data["sprites"]["front_default"]
    }
    return pokemon_info

def generate_html(pokemon_list):
    html_start = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <title>My Pokémon Team</title>
        <style>
            body { font-family: Arial, sans-serif; background: #f0f0f0; }
            .container { display: flex; flex-wrap: wrap; justify-content: center; }
            .pokemon-card {
                background: white;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
                margin: 10px;
                padding: 15px;
                width: 150px;
                text-align: center;
            }
            .pokemon-card img {
                width: 96px;
                height: 96px;
            }
            .types {
                margin-top: 10px;
            }
            .type {
                display: inline-block;
                background-color: #eee;
                border-radius: 4px;
                padding: 2px 8px;
                margin: 2px;
                font-size: 0.8em;
            }
        </style>
    </head>
    <body>
        <h1>My Favorite Pokémon Team</h1>
        <div class="container">
    """

    html_end = """
        </div>
    </body>
    </html>
    """

    cards_html = ""
    for p in pokemon_list:
        types_html = "".join([f'<span class="type">{t}</span>' for t in p["types"]])
        card = f"""
        <div class="pokemon-card">
            <img src="{p['sprite']}" alt="{p['name']} sprite" />
            <h3>{p['name']} (#{p['number']})</h3>
            <div class="types">{types_html}</div>
        </div>
        """
        cards_html += card

    return html_start + cards_html + html_end

def main():
    team_data = []
    for p in team:
        data = get_pokemon_data(p)
        if data:
            team_data.append(data)

    if not team_data:
        print("Could not fetch data for any Pokémon.")
        return

    html_content = generate_html(team_data)
    with open("my_pokemon_team.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("HTML file created: my_pokemon_team.html")

if __name__ == "__main__":
    main()
