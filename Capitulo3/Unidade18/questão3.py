def fatorial(n):
    # Caso base: 0! é 1
    if n == 0:
        return 1
    # Chamada recursiva: n! = n * (n-1)!
    return n * fatorial(n - 1)

def euler(n):
    # Caso base: quando n é 0, retorna apenas o primeiro termo da série, que é 1 (1/0! = 1)
    if n == 0:
        return 1
    # Chamada recursiva: soma 1/n! ao valor de euler(n-1)
    return 1 / fatorial(n) + euler(n - 1)

# Calculando o valor de Euler até n=20
resultado = euler(20)
# Imprimindo o resultado com 5 casas decimais
print(f'O valor aproximado de euler(20) é: {resultado:.5f}')