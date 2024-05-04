import requests

api_key ='8330db82-7d51-4c3b-8d49-6cd29402d9ce'
word ='potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

for definition in definitions:
    print(definition)