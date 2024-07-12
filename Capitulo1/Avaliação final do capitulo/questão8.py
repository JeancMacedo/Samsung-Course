print('Responda o questionário abaixo, com 1 para sim e 0 para não!')
idade = int(input('Você é maior de idade? '))
casado = int(input('Você é casado(a)? '))

if idade == 1 and casado == 1:
    print('Você é maior de idade e casado.')
elif idade == 1 and casado == 0:
    print('Você é maior de idade e solteiro.')
elif idade == 0 and casado == 1:
    print('Você é menor de idade e casado.')
elif idade == 0 and casado == 0:
    print('Você é menor de idade e solteiro.')
else:
    print('Informe corretamente, conforme descrito no inicio.')
