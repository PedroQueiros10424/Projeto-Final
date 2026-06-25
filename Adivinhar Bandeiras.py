import io, random, requests
from tkinter import *
from PIL import Image, ImageTk

janela = Tk()
janela.geometry("340x520")
janela.title("Jogo das Bandeiras")

pontos = 0
pais_atual = None

paises = [
    {"nome": "Brasil", "bandeira": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Flag_of_Brazil.svg/250px-Flag_of_Brazil.svg.png"},
    {"nome": "Portugal", "bandeira": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/250px-Flag_of_Portugal.svg.png"},
    {"nome": "Espanha", "bandeira": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/250px-Flag_of_Spain.svg.png"},
    {"nome": "Franca", "bandeira": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Flag_of_France.svg/250px-Flag_of_France.svg.png"},
    {"nome": "Italia", "bandeira": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/250px-Flag_of_Italy.svg.png"},
    {"nome": "Alemanha", "bandeira": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/250px-Flag_of_Germany.svg.png"},
    {"nome": "Reino Unido", "bandeira": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Flag_of_the_United_Kingdom.svg/250px-Flag_of_the_United_Kingdom.svg.png"},
    {"nome": "Estados Unidos", "bandeira": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Flag_of_the_United_States.svg/250px-Flag_of_the_United_States.svg.png"},
    {"nome": "Canada", "bandeira": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Flag_of_Canada.svg/250px-Flag_of_Canada.svg.png"},
    {"nome": "Argentina", "bandeira": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Flag_of_Argentina.svg/250px-Flag_of_Argentina.svg.png"},
    {"nome": "Mexico", "bandeira": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Flag_of_Mexico.svg/250px-Flag_of_Mexico.svg.png"},
    {"nome": "Japao", "bandeira": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Flag_of_Japan.svg/250px-Flag_of_Japan.svg.png"},
    {"nome": "China", "bandeira": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/250px-Flag_of_the_People%27s_Republic_of_China.svg.png"},
    {"nome": "Australia", "bandeira": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Flag_of_Australia.svg/250px-Flag_of_Australia.svg.png"},
    {"nome": "Egito", "bandeira": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Flag_of_Egypt.svg/250px-Flag_of_Egypt.svg.png"},
    {"nome": "Russia", "bandeira": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Flag_of_Russia.svg/250px-Flag_of_Russia.svg.png"},
    {"nome": "India", "bandeira": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Flag_of_India.svg/250px-Flag_of_India.svg.png"},
    {"nome": "Africa do Sul", "bandeira": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Flag_of_South_Africa.svg/250px-Flag_of_South_Africa.svg.png"},
    {"nome": "Coreia do Sul", "bandeira": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Flag_of_South_Korea.svg/250px-Flag_of_South_Korea.svg.png"},
    {"nome": "Holanda", "bandeira": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/250px-Flag_of_the_Netherlands.svg.png"},
    {"nome": "Belgica", "bandeira": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Flag_of_Belgium.svg/250px-Flag_of_Belgium.svg.png"},
    {"nome": "Suecia", "bandeira": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Flag_of_Sweden.svg/250px-Flag_of_Sweden.svg.png"},
    {"nome": "Grecia", "bandeira": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Greece.svg/250px-Flag_of_Greece.svg.png"},

]

lista_restantes = list(paises)


def proxima_bandeira():
    global pais_atual, lista_restantes
    caixa_texto.config(state="normal")
    if not lista_restantes:
        texto_feedback.config(text=f"Fim do jogo! Pontuação: {pontos}")
        caixa_texto.config(state="disabled")
        return
    pais_atual = random.choice(lista_restantes)
    lista_restantes.remove(pais_atual)
    try:

        dados_imagem = requests.get(pais_atual["bandeira"], headers={'User-Agent': 'Jogo das bandeiras'}, timeout=5).content
        imagem_ecra.image = ImageTk.PhotoImage(Image.open(io.BytesIO(dados_imagem)).resize((250, 150)))
        imagem_ecra.config(image=imagem_ecra.image)
    except:
        proxima_bandeira()
        return
    caixa_texto.delete(0, END)
    texto_feedback.config(text="")


def validar_resposta():
    global pontos
    if not pais_atual: return
    caixa_texto.config(state="disabled")

    if caixa_texto.get().strip().lower() == pais_atual["nome"].lower():
        pontos += 1
        texto_feedback.config(text="Correto!")
        texto_pontos.config(text=f"Pontos: {pontos}")
    else:
        texto_feedback.config(text=f"Falhaste... era: {pais_atual['nome']}")

    janela.after(1500, proxima_bandeira)


janela.columnconfigure(0, weight=1)

Label(janela, text="Adivinha o País").grid(row=0, column=0, pady=5)
texto_pontos = Label(janela, text="Pontos: 0")
texto_pontos.grid(row=1, column=0, pady=5)

imagem_ecra = Label(janela)
imagem_ecra.grid(row=2, column=0, pady=10)

caixa_texto = Entry(janela)
caixa_texto.grid(row=3, column=0, pady=5)
caixa_texto.bind("<Return>", lambda e: validar_resposta())

texto_feedback = Label(janela, text="")
texto_feedback.grid(row=4, column=0, pady=5)

Label(janela, text="(Não precisa de acentos)").grid(row=5, column=0, pady=5)
Button(janela, text="Submeter", command=validar_resposta).grid(row=6, column=0, pady=5)

proxima_bandeira()
janela.mainloop()