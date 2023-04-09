import requests
Token = "bbc889aa591cdccdc64f64f5e6b80e2f"
Url = "https://pokemonbattle.me:9104/"

# регистрация тренера
response_trainer_reg = requests.post (f"{Url}trainers/reg", json= {
    "trainer_token": Token,
    "email": "ill-istjagin-sergej@qa.studio",
    "password": "qT4H-6TEXq4J5v-zegiO"
})
print(response_trainer_reg.text)

# активация тренера
response_confirm_email = requests.post (f"{Url}trainers/confirm_email", json= {
    "trainer_token": Token
})
print(response_confirm_email.text)

# создание покемона
response_add_pokemon = requests.post (f"{Url}pokemons", headers = {"trainer_token": Token}, json= {
    "name": "Взрыван",
    "photo": "https://dolnikov.ru/pokemons/albums/050.png"
})
print(response_add_pokemon.text)

# переименование покемона? смена картинки
response_rename_pokemon = requests.put (f"{Url}pokemons", headers = {"trainer_token": Token}, json= {
    "pokemon_id": "8855",
    "name": "ЫХЫХЫХЫ",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
})
print(response_rename_pokemon.text)

# ловля покемона
response_catch_pokemon = requests.post (f"{Url}trainers/add_pokeball", headers = {"trainer_token": Token}, json= {
    "pokemon_id": "8855",
})
print(response_catch_pokemon.text)