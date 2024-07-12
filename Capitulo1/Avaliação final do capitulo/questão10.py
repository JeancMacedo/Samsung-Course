print('1 opção de resolução:\n')
def armstrong(n):
    # Converte o número para string para separar os dígitos
    digitos = [int(d) for d in str(n)]
    # Calcula a soma dos cubos dos dígitos
    soma_cubos = sum([d**3 for d in digitos])
    # Verifica se a soma dos cubos é igual ao número
    return soma_cubos == n

# Itera pelos números de 100 a 999
for num in range(100, 1000):
    if armstrong(num):
        print(num)
print('\n\n2 opção de resolução:\n')

for num in range(100, 1000):
    # Separar os dígitos do número
    centena = num // 100
    dezena = (num // 10) % 10
    unidade = num % 10
    
    # Calcular a soma dos cubos dos dígitos
    soma_cubos = centena**3 + dezena**3 + unidade**3
    
    # Verificar se o número é um número Armstrong
    if soma_cubos == num:
        print(num)
print('\n')
