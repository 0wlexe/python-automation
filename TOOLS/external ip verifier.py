# Ferramenta para verificaçao do ip externo de uma maquina

import re
import json
from urllib.request import urlopen

url = 'http://ipinfo.io/json'

response = urlopen(url)

data = json.load(response)

ip = data['ip']
org = data['org']
city = data['city']
country = data['country']
region = data['region']

print("Detalhes do IP externo\n")
print("IP: {4} \nRegião: {1}\nPais: {2}\nCidade: {3}\nOrg: {0}".format(org,region,country,city,ip))