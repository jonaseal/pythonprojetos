import requests
import json

url = 'https://www.w3schools.com/python/demopage.php'
objeto = {
	"cadastrarvaga": [
	  {
		"id": 1,
		"dadosdaempresa": {
            "cnpj": "84101722000122",  
            "razão social": "CUBOBPM",
            "nome fantasia": "CUBOBPM",
            "cep ":"74645010",
            "endereco":"Avenida Independencia",
            "numero":"12345",
            "complemento": "Apartamento",
            "bairro": "Vila Nova",
            "municipio": "Goiânia",
            "uf": "Goiás",
            "empresafoinotificada":"Sim"          
            },

		"caracteristicasdavaga": {

            "permitircandidaturas": "Sim",
            "permitircandiporlocal": "Sim",
            "periododecandiinicio":"31/03/2022",
            "períododecandifim:":"01/04/2022",
            "cidadeestadooubairro":"Goiás",
            "numerojovens":"10",
            "cargooferecido": "Programador",
            "genero": "Homem",
            "faixaetariaminima": "18",
            "faixaetariamaxima": "56",
            "tercompletidademinimaate": "Sim",
            "beneficios": ["Transporte","Alimentação","P Saúde","P Odontológico"],
            "condicoes":["Insalubre", "Perigoso"],
            "descricaodasatividades": "Vaga criada por robo (RPA)"

        },
		"sobreocontrato": {

            "datadacontratacao": "22/03/2022",
            "remuneracao": "100000",
            "vagadesubstuicao":"Sim"
        },
		"dadosdaselecao": {

            "dataselecao": "30/03/2022",
            "nomedoresponsavel":"Carlos",
            "cargo": "Programador",
            "telefone":"62992542458",
            "e-mail":"teste@gmail.com",
            "localdeselecao":"Presencial",
            "linkdareuniao":"www.teste.com"

        },
		"perfiljovem": {
            "tipocontrato":"Estágio",
            "escolaridade":"Básico",
            "serie":"N1",
            "cursos":["Programação","Administração"],
            "perfilcomportamental":["Inovador","Comunicativo", "Empatia","Gostar de números", "Detalhista"]

        },
		"provas": {
            "queroaplicar":"Sim",
            "provas":["Português", "Matemática"],
            "aplicarredacao":"Sim",
            "temaredacao":["teste"]
        }
        
	  }
	]
    
}


#resultado = requests.post(url, data = myobj)

print(objeto['cadastrarvaga'][0]['caracteristicasdavaga']['beneficios'])