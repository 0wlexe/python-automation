import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 4)
# 4 = UDP
print("Cliente socket criado com sucesso!")

host = 'localhost'
port = 5433 # porta a ser conectada no servidor
message = "Hi server!" # mensagem a ser enviada

try:
    print("Client: " + message)
    s.sendto(message.encode(), (host, 5432))

    dados, servidor = s.recvfrom(4096) 
    dados =  dados.decode()
    print("Client: " + dados)
finally:
    print("Client: fechando a conexão")
    s.close()