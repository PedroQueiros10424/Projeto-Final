import requests
import json
from tkinter import *
import random
from PIL import Image

janela = Tk()
janela.geometry("350x400+75+30")
janela.title("Jogo dad Bandeiras")


import requests
response = requests.get(
  "https://api.restcountries.com/countries/v5?limit=30&response_fields=names.common,flag.url_png",
  headers={'Authorization': 'Bearer rc_live_8e8181308e8a48c38b8ac7858fa6f54a'}
)

dados = response.json()
print(dados)

# Print the response

with open("dados_api.json", "w", encoding="utf-8") as ficheiro:
    json.dump(dados, ficheiro, ensure_ascii=False, indent=4)

for pais in dados["data"]["objects"]:
    nome = pais["names"]["common"]
    bandeira = pais["flag"]["url_png"]

paises = []

for pais in dados["data"]["objects"]:
    paises.append({
        "nome": pais["names"]["common"],
        "bandeira": pais["flag"]["url_png"]
    })
pais_atual = random.choice(paises)

imagem_url = requests.get(pais_atual["bandeira"]).content

imagem = Image.open((imagem_url))
imagem = imagem.resize((200,120))



janela.mainloop()