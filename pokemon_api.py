import requests
import json

api_url = "https://pokeapi.co/api/v2/pokemon?limit=20&offset=0"

class Pokemon():
    def __init__(self, abilities, types, name, weight):
        self.abilities = abilities
        self.types = types
        self.name = name
        self.weight = weight
    
    def get_data(self, api_url):
        response = requests.get(api_url)
        data = response.json()

        # Loop through the list of Pokemon
        for result in data['results']:
            pokemon_details = requests.get(result['url']).json()

            # Extract relevant information
            self.name = pokemon_details['name']
            self.abilities = [ability['ability']['name'] for ability in pokemon_details['abilities']]
            self.types = [type['type']['name'] for type in pokemon_details['types']]
            self.weight = pokemon_details['weight']

            # Print information for each Pokemon
            print(f"Name: {self.name}")
            print(f"Abilities: {', '.join(self.abilities)}")
            print(f"Types: {', '.join(self.types)}")
            print(f"Weight: {self.weight}")
            print("\n")

pokemon_instance = Pokemon(abilities=[], types=[], name="", weight=0)
pokemon_instance.get_data(api_url)
