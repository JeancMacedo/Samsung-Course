# Solicita ao usuário o tamanho da matriz (n x n)
n = int(input("Informe o tamanho da matriz (n ≥ 2): "))

# Verifica se o tamanho é válido (n ≥ 2)
if n < 2:
    print("Por favor, informe um valor maior ou igual a 2.")
else:
    # Cria a matriz quadriculada
    matriz = [[(j + i) % 2 for i in range(n)] for j in range(n)]
    
    # Exibe a matriz
    for linha in matriz:
        print(linha)