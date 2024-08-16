numeros = (1, 2, 5, 4, 3, 2, 1, 4, 7, 8, 9, 9, 3, 7, 3, 9)

elemento_mais_frequente = numeros[0]
max_ocorrencias = numeros.count(numeros[0])

# Iterar por todos os elementos da tupla
for numero in numeros:
    ocorrencias = numeros.count(numero)
    
    if ocorrencias > max_ocorrencias or (ocorrencias == max_ocorrencias and numero > elemento_mais_frequente):
        elemento_mais_frequente = numero
        max_ocorrencias = ocorrencias

print(f"O elemento que ocorre o maior número de vezes é: {elemento_mais_frequente}")