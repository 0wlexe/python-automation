# Ferramenta gráfica de botão para abrir o navegador

import webbrowser
from tkinter import *

root = Tk( )

root.title("Abrir browser")
root.geometry('250x60')

def duckduckgo():
    webbrowser.open('https://duckduckgo.com/')

myduck = Button(root, text = "Abrir o DuckDuckGo", command=duckduckgo).pack(pady=20)
root.mainloop()

