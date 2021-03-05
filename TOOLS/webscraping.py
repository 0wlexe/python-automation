# Coletor de dados webscraping

from bs4 import BeautifulSoup 
import requests 

site = requests.get("https://siteurl.com.br/").content
# objetp site recebendo o conteudo da requisiçao http do site de escolha
soup = BeautifulSoup(site, 'html.parser')
# objeto soup baixando o html do site
print(soup.prettify()) 
# prettitfy transforma o html em string e o print vai exibir o html 

'''
# Outros comandos 

temperatura = soup.find("span", class_="_block _margin-b-5 -gray")
# Procurar classes em especifico

print(temperatura.string)
# Transorma a estrutura html em string e a imrpime 

print(soup.title.string) 
# Para mostar apenas o que tem dentro dos titulos 

print(soup.find('admin')) 
# Para achar coisas relacionadas ao admin da pagina

'''