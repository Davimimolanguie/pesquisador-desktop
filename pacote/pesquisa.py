import requests
from tkinter import *
def pesquisar(resolvido,janela1):
    ir = requests.get("https://pt.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&titles="+resolvido+"&exintro=true&explaintext=true")
    if ir.status_code == 200:
        data = ir.json()
        pages = data["query"]["pages"]
        page = list(pages.values())[0]
        if "missing" in page or not page.get("extract"):  # Verifica se a página não existe ou não tem 'extract'
            resolvido = resolvido.replace(" ", "_")
            ir = requests.get("https://pt.wikipedia.org/wiki/"+resolvido.title())
            pesquisouja = ir.text
            posinicial = pesquisouja.find("<p><b>", 0)  # Localiza a abertura "<"     
            posfinal = pesquisouja.find(".", posinicial)  # Localiza o fechamento ">"
            pesquisouja = pesquisouja[posinicial:posfinal + 1]  # Inclui o ">"
            if "<b>A Wikipédia não possui um artigo com este nome exato.</b>" in ir.text or ir.text == "":
                erro = Label(janela1, text="nada encontrado" ,bg="black", fg="white", wraplength=200).grid(row=4, column=0)
            else:
                html = []
                start = 0
                while "<" in pesquisouja and ">" in pesquisouja:
                    posinicial = pesquisouja.find("<")
                    posfinal = pesquisouja.find(">", posinicial)
                    if posfinal == -1:
                        break  # Garante que não ocorra erro se não houver ">"
                    pesquisouja = pesquisouja[:posinicial] + pesquisouja[posfinal + 1:]
                exito = Label(janela1, text=pesquisouja ,bg="black", fg="white", wraplength=200).grid(row=4, column=0)
        else:
            texto = page["extract"]
            exito = Label(janela1, text=texto ,bg="black", fg="white", wraplength=200).grid(row=4, column=0)
    else:
        erro = Label(janela1, text="erro" ,bg="black", fg="white", wraplength=200).grid(row=4, column=0)
