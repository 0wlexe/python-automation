import itertools

string = input("String a ser permutada: ")
resultado = itertools.permutations(string, len(string)) 
# len(string) pega o tamanho da variavel string

for i in resultado:
    print(''.join(i))