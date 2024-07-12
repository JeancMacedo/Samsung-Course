print("Bem vindo a calculadora, informe o simbolo e dois numeros!")
print('\nSimbolos: "*" para multiplicação, "+" para adição, \
"-" para subtração e "/" para divisão.')
simbolo = input('\nDigite o simbolo: ')
n1 = input('Digite o primeiro número: ')
n1 = int(n1)
n2 = input('Digite o segundo  número: ')
n2 = int(n2)
calculo = 0
if ( simbolo == '*'):
    calculo = n1 * n2
    print(f'\nResultado da multiplicação é: {calculo}')
elif ( simbolo == '/'):
    calculo = n1 / n2
    print(f'\nResultado da divisão é: {calculo}')
elif ( simbolo == '+'):
    calculo = n1 + n2
    print(f'\nResultado da adição é: {calculo}')  
elif ( simbolo == '-'):
    calculo = n1 - n2
    print(f'\nResultado da subtração é: {calculo}')  