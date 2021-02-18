import os 
#Biblioteca 'os' que integra os programas e recursos do sistema operacional

ip_ou_host = input("Digite o ip ou host a ser verificado: ") 
#variavel que recebe o ip

os.system('ping -n 6 {}'.format(ip_ou_host)) 
#chamando metodo system da biblioteca os para rodar o comando ping
print("-" * 60)
#imprime o traço '-' 60 vezes

