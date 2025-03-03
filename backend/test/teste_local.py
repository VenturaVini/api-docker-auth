import requests


url = 'http://localhost:7324'


requisicao = requests.get(url)
print(requisicao.json())


def pegar_token(usuario, senha):
    url = 'http://localhost:7324/auth/login'
    payload = {
        'username': usuario,
        'senha': senha
    }
    requisicao = requests.post(url, json=payload)
    return requisicao.json()


token = pegar_token('vini', '123')['access_token']

url_post = url + '/produtos/'

payload = {
    'id': 3,
    'nome': 'Iphone 15 128GB',
    'descricao': 'teste',
    'preco': 4499.99,
    'estoque': 17,
}

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

requisicao_post = requests.post(url_post, json=payload, headers=headers)
print(requisicao_post.json())


requisicao = requests.get(url)
print(requisicao.json())

