numero = 51
numero = int(numero)
print('Adivinhe um número entre 1 e 100!\n')
tentativa = 1
tentativas = int(input('Digite um número: '))

while tentativas != numero:
    tentativas = int(input('Digite um número: '))
    tentativa += 1
    if tentativas == numero:
        print('\nVoce acertou, Parabéns!')
        print(f'Total de tentativas: {tentativa}')