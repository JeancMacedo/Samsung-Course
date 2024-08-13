# Definindo a tupla com as notas
notas = (('Davi',  88,  95, 90), ('Felipe', 83, 98, 81), ('Luciano', 81, 97, 98), ('Rodrigo', 82, 89, 83))

# Usando zip para agrupar as notas de cada matéria
_, notas_ingles, notas_matematica, notas_ciencia = zip(*notas)

# Calculando a média das notas de matemática
media_matematica = sum(notas_matematica) / len(notas_matematica)

# Imprimindo a média das notas de matemática
print(f"A média das notas de matemática é: {media_matematica:.2f}")