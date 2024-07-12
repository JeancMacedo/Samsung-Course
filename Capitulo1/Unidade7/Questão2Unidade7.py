print('Informe dois números e veja se o primeiro é um \
multiplo do segundo.')
print('\n')
numero_A = input("Informe um número: ")
numero_A = int(numero_A)
numero_B = input("Informe outro número: ")
numero_B = int(numero_B)

if (numero_A % numero_B) == 0:
    print(f"\nO número {numero_A} é multiplo de {numero_B}\n\n")
else:
    print(f"\nO número {numero_A} não é multiplo de {numero_B}\n\n")