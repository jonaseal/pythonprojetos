import requests
import json

url = 'https://www.w3schools.com/python/demopage.php'
objeto = {
    "type": "object",
    "properties": {
        "cadastrarvaga": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer"
                    },
                    "dadosdaempresa": {
                        "type": "object",
                        "properties": {
                            "cnpj": {
                                "type": "string"
                            },
                            "razão social": {
                                "type": "string"
                            },
                            "nome fantasia": {
                                "type": "string"
                            },
                            "cep ": {
                                "type": "string"
                            },
                            "endereco": {
                                "type": "string"
                            },
                            "numero": {
                                "type": "string"
                            },
                            "complemento": {
                                "type": "string"
                            },
                            "bairro": {
                                "type": "string"
                            },
                            "municipio": {
                                "type": "string"
                            },
                            "uf": {
                                "type": "string"
                            },
                            "empresafoinotificada": {
                                "type": "string"
                            }
                        }
                    },
                    "caracteristicasdavaga": {
                        "type": "object",
                        "properties": {
                            "permitircandidaturas": {
                                "type": "string"
                            },
                            "permitircandiporlocal": {
                                "type": "string"
                            },
                            "periododecandiinicio": {
                                "type": "string"
                            },
                            "períododecandifim:": {
                                "type": "string"
                            },
                            "cidadeestadooubairro": {
                                "type": "string"
                            },
                            "numerojovens": {
                                "type": "string"
                            },
                            "cargooferecido": {
                                "type": "string"
                            },
                            "genero": {
                                "type": "string"
                            },
                            "faixaetariaminima": {
                                "type": "string"
                            },
                            "faixaetariamaxima": {
                                "type": "string"
                            },
                            "tercompletidademinimaate": {
                                "type": "string"
                            },
                            "beneficios": {
                                "type": "string"
                            },
                            "condicoes": {
                                "type": "string"
                            },
                            "descricaodasatividades": {
                                "type": "string"
                            }
                        }
                    },
                    "sobreocontrato": {
                        "type": "object",
                        "properties": {
                            "datadacontratacao": {
                                "type": "string"
                            },
                            "remuneracao": {
                                "type": "string"
                            },
                            "vagadesubstuicao": {
                                "type": "string"
                            }
                        }
                    },
                    "dadosdaselecao": {
                        "type": "object",
                        "properties": {
                            "dataselecao": {
                                "type": "string"
                            },
                            "nomedoresponsavel": {
                                "type": "string"
                            },
                            "cargo": {
                                "type": "string"
                            },
                            "telefone": {
                                "type": "string"
                            },
                            "e-mail": {
                                "type": "string"
                            },
                            "localdeselecao": {
                                "type": "string"
                            },
                            "linkdareuniao": {
                                "type": "string"
                            }
                        }
                    },
                    "perfiljovem": {
                        "type": "object",
                        "properties": {
                            "tipocontrato": {
                                "type": "string"
                            },
                            "escolaridade": {
                                "type": "string"
                            },
                            "serie": {
                                "type": "string"
                            },
                            "cursos": {
                                "type": "array"
                            },
                            "perfilcomportamental": {
                                "type": "array"
                            }
                        }
                    },
                    "provas": {
                        "type": "object",
                        "properties": {
                            "queroaplicar": {
                                "type": "string"
                            },
                            "provas": {
                                "type": "array"
                            },
                            "aplicarredacao": {
                                "type": "string"
                            },
                            "temaredacao": {
                                "type": "string"
                            }
                        }
                    }
                },
                "required": [
                    "id",
                    "dadosdaempresa",
                    "caracteristicasdavaga",
                    "sobreocontrato",
                    "dadosdaselecao",
                    "perfiljovem",
                    "provas"
                ]
            }
        }
    }
}

#resultado = requests.post(url, data = myobj)

print(objeto['cadastrarvaga'])