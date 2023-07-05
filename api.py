print('read api')
import requests
paginaresults = requests.get('https://catfact.ninja/facts')
feitjes = paginaresults.json()
#print(feitjes)
print(feitjes["data"][0])