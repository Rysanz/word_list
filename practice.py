# import requests

# api_key = '84c1362e-4cc7-4bcf-9631-fdc8aabdd7ce'
# word = 'potato'
# url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'


# res = requests.get(url)

# definitions = res.json()

# print(definitions)

# for definition in definitions:
#     print(definition)

import requests

api_key = '84c1362e-4cc7-4bcf-9631-fdc8aabdd7ce'
word = 'voluminous'
root_url = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json'
final_url = f'{root_url}/{word}?key={api_key}'
r = requests.get(final_url)
result = r.json()
print(result)