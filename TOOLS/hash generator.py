import hashlib

string = input("\n Digite o texto a ser convertido: ")

menu = int(input('''\n ### Agora escolha o tipo de hash ### \n
               1) MD5
               2) SHA1
               3) SHA256
               4) SHA512
            \n Qual o número do hash a ser gerado? '''))

if menu == 1:
    resultado = hashlib.md5(string.encode('utf-8'))
    print("\n O hash MD5 da string ", string, "é:", resultado.hexdigest())

elif menu == 2:
    resultado = hashlib.sha1(string.encode('utf-8'))
    print("\n O hash SHA1 da string", string, "é:", resultado.hexdigest())

elif menu == 3:
    resultado = hashlib.sha256(string.encode('utf-8'))
    print("\n O hash SHA256 da string", string, "é:", resultado.hexdigest())

elif menu == 4:
    resultado = hashlib.sha512(string.encode('utf-8'))
    print("\n O hash SHA512 da string", string, "é:", resultado.hexdigest())

else:
    print("\n Esse número não existe, tente novamente! :(\n")