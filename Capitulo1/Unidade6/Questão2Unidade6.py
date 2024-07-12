print("Informe um número de -100, 1 e 100")
n = input('Digite o número: ')
n = int(n)

if (n >= -100 and n <= -1):
    print('x = ', n)
    print(f'{n} não é um número natural.')
elif(n >= 0 and n <= 100):
    print('x = ', n)
    print(f'{n} é um número natural.')