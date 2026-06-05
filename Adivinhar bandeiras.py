import requests
import json

# The API endpoint
url = "  https://restcountries.com/v3.1/all?fields=name,flags"

# A GET request to the API
response = requests.get(url)
dados = response.json()

# Print the response
print(response.json())
with open("dados_api.json", "w", encoding="utf-8") as ficheiro:
    json.dump(dados, ficheiro, ensure_ascii=False, indent=4)

