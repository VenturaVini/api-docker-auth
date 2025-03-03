import requests


separador = '-----------------------------------------------------------------------------------'

url = 'https://api-auth-vini.up.railway.app/'

coletar = requests.get(url=url)

print(coletar.json())


print(separador)


url_modificar = f'{url}produtos/'

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkcmV3IiwiZXhwIjoxNzM5NTQ1Njk4fQ.pYihtD41G023qOrr7yXztdsGMdqGPWLQvXT4hycnU8A"

# Cabeçalhos
headers = {
    "Content-Type": "application/json",
    "Authorization": token
}

dados = {
    'id' : 2,
    'nome': 'Iphone 20 128gb',
    'descricao': 'ainda vai existir',
    'preco': 1000000,
    'estoque': 1
}

alterar = requests.put(url= url_modificar, headers= headers, json= dados )

print("Status Code:", alterar.status_code)
print("Response Text:", alterar.text)

print(alterar.json())


print(separador)


coletar = requests.get(url=url)

print(coletar.json())