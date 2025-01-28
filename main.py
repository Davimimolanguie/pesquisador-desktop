from pacote.definir import decum, decdois

from functools import partial
from pacote.replace import subs
from pacote.pesquisa import pesquisar
from tkinter import *
import requests
from bs4 import BeautifulSoup
janela1=Tk()
janela1.configure(bg="black")
janela1.geometry("800x600")
ola = Label(janela1, text="olá! clique onde que você quer" ,bg="black", fg="white").grid(row=0, column=0)
opdois = Button(janela1, text="fazer uma pesquisa", command=partial(decum, janela1)).grid(row=0, column=1)
opdois=Button(janela1, text="ver a previsão", command=partial(decdois, janela1)).grid(row=0, column=2)
janela1.mainloop()