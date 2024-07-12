print("Digite um número inteiro, caso ele seja múltiplo \
de 5, \nserá retornado com True, caso contrário False.")
n = input("Informe um número: ")
n = int(n)

if (n % 5 == 0):
    n = True
    print(n)
else:
    n = False
    print(n)