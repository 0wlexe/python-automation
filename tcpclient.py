import socket 
#socket  = relaciona placa de rede e sistema operacional
import sys 
#fornece acesso de variaveis e funcoes que tem relaçao com o interpretador(python)

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        #0 = protocolo tcp 
    except socket.error as error:
        print("A conexão falhou!")
        print("Erro: {}".format(error))
        sys.exit() #encerra o programa em caso de erros
    
    print("Socket criado com sucesso!") #se nao ocorrer erro

    targetHost = input("Digite o Host ou Ip a ser conectado: ")
    targetPort = input("Digite a porta a ser conectada: ")

    try:
        s.connect((targetHost, int(targetPort))) #faz a conexao, transforma a porta em string
        print("Cliente TCP conectado no host " + targetHost + " com excito!")
        s.shutdown(2) #espera dois segundos para encerrar a conexao e não a deixar em loop
    except socket.error as error:
        print("A conexão falhou!")
        print("Erro: {}".format(error))
        sys.exit()

if __name__ == "__main__":
    main()