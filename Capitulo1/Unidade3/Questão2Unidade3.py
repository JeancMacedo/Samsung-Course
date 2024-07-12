# Solicita ao usuário para inserir um número
numero = int(input("Informe um número: "))

# Verifica se o número é negativo
if numero < 0:
    print("O fatorial não é definido para números negativos.")
elif numero == 0 or numero == 1:
    # O fatorial de 0 e 1 é 1
    print(f"O fatorial de {numero} é 1")
else:
    # Calcula o fatorial
    fatorial = 1
    for i in range(2, numero + 1):
        fatorial *= i
    # Exibe o resultado
    print(f"O fatorial de {numero} é {fatorial}")