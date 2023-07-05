print('We gaan scrapen')
import requests

from bs4 import BeautifulSoup
pagina=requests.get('https://coinmarketcap.com')

heeldehtml= BeautifulSoup(pagina.content,'html.parser')
body=heeldehtml.find('tbody')

print(body.prettify())