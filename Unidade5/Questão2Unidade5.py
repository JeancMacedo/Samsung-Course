numero = input("Informe um número dentre 0 a 100: ")
numero = int(numero)

if ( numero % 2 == 0 and numero >= 0 and numero <= 100):
    numero = True
    print(numero)
else:
    numero = False
    print(numero)