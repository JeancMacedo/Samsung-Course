print('True para é impar, False para é par.')
numero = input("Informe um número e descubra se ele é impar: ")
numero = int(numero)
if (numero % 2 == 1):
    numero = True
    print(numero)
else:
    numero = False
    print(numero)