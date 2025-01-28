from tkinter import *
import requests
from pacote.replace import subs
from pacote.pesquisa import pesquisar
pesquisa = ""  
def bot(janela1):
    resolvido = subs(pesquisa)
    pesquisar(resolvido, janela1)
def decum(janela1):
    texput = Label(janela1, text="digite sua pesquisa evite formar frases", bg="black", fg="white")
    texput.grid(row=2, column=0)
    input_entry = Entry(janela1)  
    input_entry.grid(row=3, column=0)
    def atualizar_pesquisa():
        global pesquisa
        pesquisa = input_entry.get()
    botao = Button(janela1, text="enter", command=lambda: [atualizar_pesquisa(), bot(janela1)])  # Atualiza a pesquisa antes de chamar a função bot
    botao.grid(row=3, column=1)
def decdois(janela1):
    graus = requests.get("https://weather.com")
    if graus.status_code == 200:
        posinicial = graus.text.find("<span data-testid=\"TemperatureValue\" class=\"CurrentConditions--tempValue--zUBSz\" dir=\"ltr\">", 0)
        posfinal = graus.text.find("<span class=\"CurrentConditions--degreeSymbol--tzLy9\">°</span><span></span></span>", posinicial)
        substring = graus.text[posinicial:posfinal]
        substring = substring.replace("<span data-testid=\"TemperatureValue\" class=\"CurrentConditions--tempValue--zUBSz\" dir=\"ltr\">", "")
        previsao = Label(janela1, text="no brasil faz " + substring + " graus", bg="black", fg="white")
        previsao.grid(row=4, column=0)
    else:
        erro = Label(janela1, text="erro ao ver a previsão", bg="black", fg="white")
        erro.grid(row=4, column=0)