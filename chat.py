import requests
import json
from tkinter import *
import random
from PIL import Image, ImageTk
from io import BytesIO


janela = Tk()
janela.geometry("350x450+75+30")
janela.title("Jogo das Bandeiras")



import requests
response = requests.get(
  "https://api.restcountries.com/countries/v5?limit=30&response_fields=names.common,flag.url_png",
  headers={'Authorization': 'Bearer rc_live_8e8181308e8a48c38b8ac7858fa6f54a'}
)

a = response.json()
print(a)
b= a["data"]["objects"]

print(b)

with open("dados_api.json", "w", encoding="utf-8") as ficheiro:
    json.dump(a, ficheiro, ensure_ascii=False, indent=4)



paises = []

for pais in b:
    if "flag" in pais:
        paises.append({
            "nome": pais["names"]["common"],
            "bandeira": pais["flag"]["url_png"]
        })

print(paises)

pais_atual = random.choice(paises)


imagem_url = requests.get(
    pais_atual["bandeira"]
).content



imagem = Image.open(
    BytesIO(imagem_url)
)

imagem = imagem.resize((200, 120))



bandeira = ImageTk.PhotoImage(imagem)


label_imagem = Label(
    janela,
    image=bandeira
)

label_imagem.image = bandeira
label_imagem.pack(pady=20)




texto = Label(
    janela,
    text="Que país é este?"
)

texto.pack()



entrada = Entry(janela)
entrada.pack()


# resultado
resultado = Label(janela, text="")
resultado.pack(pady=10)



def verificar():

    resposta = entrada.get()

    if resposta.lower() == pais_atual["nome"].lower():
        resultado.config(text="Correto!")

    else:
        resultado.config(
            text=f"Errado! Era {pais_atual['nome']}"
        )



botao = Button(
    janela,
    text="Responder",
    command=verificar
)

botao.pack()



janela.mainloop()