import requests
import json

url = 'https://www.w3schools.com/python/demopage.php'
arquivo = open('cadastrarvaga.json',encoding='utf-8')
objeto = json.load(arquivo)
#resultado = requests.post(url, data = objeto)
#print(resultado.status_code)
print(objeto['cadastrarvaga'][0]['dadosdaempresa']['cnpj'])