# Ferramenta para a ocultaçao de pastas 

import ctypes

pasta = input("Digite o caminho da pasta a ser ocultada (Ex: C:/pasta): ")

atributo_ocultar = 0x02 #Atributo decimal que indica que o arquivo sera ocultado

retorno = ctypes.windll.kernel32.SetFileAttributesW(pasta, atributo_ocultar)

if retorno:
    print("A pasta foi ocultado!")
else:
    print("A pasta não foi ocultado!")
