import copy

# Declarando o dicionário school
school = {
    'kim': {'age': 16, 'hei': 170, 'grade': 3},
    'lee': {'age': 15, 'hei': 168, 'grade': 2},
    'choi': {'age': 14, 'hei': 173, 'grade': 1}
}

# Fazendo uma cópia do dicionário school
school2 = copy.deepcopy(school)

# Verificando se school e school2 são variáveis diferentes
print(school is school2)  # Isso deve imprimir False
print(school)
print('*'*10)
print(school2)