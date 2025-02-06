import requests

url = 'https://api.pokemonbattle.ru/v2'
token = 'bbfb55b3398587eba9f4fe46e66ef762'
header = {'Content-Type' : 'application/json', 'trainer_token' : token}

body_pokemon_create = {
        "name": "TESTNAME",
        "photo_id": 1
}

body_poremon_rename = {
    "pokemon_id": "666666",
    "name": "TESTNAME",
    "photo_id": 1
}

body_pokemon_catch_in_pokeball = {
    "pokemon_id": "666666"
}

# Создание покемона
response_create = requests.post(url = f'{url}/pokemons', headers = header, json = body_pokemon_create)
print(response_create.text)

# Изменение покемона
response_rename = requests.put(url = f'{url}/pokemons', headers = header, json = body_poremon_rename)
print(response_rename.text)

# Поймать покемона в покеболл
response_catch_in_pokeball = requests.post(url = f'{url}/trainers/add_pokeball', headers = header, json = body_pokemon_catch_in_pokeball)
print(response_catch_in_pokeball.text)