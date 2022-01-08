import requests

# retorno = requests.post("http://127.0.0.1:8000/usuario")
retorno = requests.post("http://127.0.0.1:8000/inserir", params={'':7, 'nome':'usuario', 'senha':'senha'})
print(retorno.json())