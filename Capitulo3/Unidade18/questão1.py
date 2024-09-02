n = 0
n = int(input("Informe um número: "))
soma = 0
for i in range(1,n+1):
    soma += i
print(f'A soma de 1 a {n} é {soma}')

print('**'*10)

def soma_recursiva(n):
    # Caso base: se n for 1, retorna 1
    if n == 1:
        return 1
    # Chamada recursiva: soma o valor atual de n com a soma dos números anteriores
    return n + soma_recursiva(n - 1)

# Exemplo de uso:
n = int(input("Digite um número: "))
print("A soma de 1 a", n, "é:", soma_recursiva(n))