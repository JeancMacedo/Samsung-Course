# Inicializa a soma
soma = 0

# Itera pelos números de 1 a 100
for i in range(1, 101):
    # Verifica se o número é ímpar
    if i % 2 != 0:
        # Adiciona o número ímpar à soma
        soma += i

# Imprime a soma dos números ímpares
print("A soma dos números ímpares de 1 a 100 é:", soma)