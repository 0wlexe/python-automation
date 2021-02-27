import random, string

size = int(input('Digite o tamanho da senha que você deseja: ')) 

chars = string.ascii_letters  + string.digits + '!@#$%&8()-+,;:/?'
# recebe a estrutura da senha a ser gerada

rnd = random.SystemRandom() 
# os.urandom - gera numeros aleatorios a partir de fontes fornecidas pelo sistema operacional

print(''.join(rnd.choice(chars) for i in range(size)))
# retorna uma lista com os caracteres randomicos gerado pelo chars com a quantidade de caracteres de size

