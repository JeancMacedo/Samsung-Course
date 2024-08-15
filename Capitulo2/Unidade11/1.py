pessoa = {'Nome': 'David Doe', 'Idade': 26, 'Peso': 82} #Dicionário com nome, idade, peso
print(pessoa['Nome'])

estudantes = {2019001: 'John Smith', 2019002: 'Jane Carter', 2019003: 'Peter Kelly'}
print(estudantes[2019001])

del estudantes[2019002]
print(estudantes)

#NO CAPITULO ATUAL MOSTRA COMO ADICIONAR IMPORT JSON!
"""
exemplo abaixo
"""

"""
import json
data =  '{"Título": "O Velho e o Mar", "ISBN": "12345", "Autor": "Ernest Hemingway"}'
json_data = json.loads(data)

# Código para criar json_ data como arquivo book.json
with open('book.json', 'w') as f:
  json.dump(json_data, f, indent='\t')
"""
