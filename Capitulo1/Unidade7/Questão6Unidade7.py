print('Bem-vindo a um delicioso restaurante.\
Aqui está o cardápio:\n \
    \nHambúrguer(digite H)\
    \nFrango(digite F)\
    \nPizza(digite P) \n')
pedido = input('\nDigite o caracter desejado: ')

if( pedido == 'H' or pedido == 'h'):
    print('Voce pediu Hambúrguer')
elif( pedido == 'F' or pedido == 'f'):
    print('Você pediu Frango.')
elif( pedido == 'P' or pedido == 'p'):
    print('Você pediu Pizza.')
else:
    print("Informe um pedido válido.")