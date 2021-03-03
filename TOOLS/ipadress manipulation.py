import ipaddress

ip = '0.0.0.0/24' # Coloque o ip desejado
rede = ipaddress.ip_network(ip, strict=False)

for ip in rede:
    print(rede)