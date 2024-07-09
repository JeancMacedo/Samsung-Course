print('Bem vindo ao programa que mostra coordenadas.\n')
coordenadasx = input('Informe a coordenada de x: ')
coordenadasx = int(coordenadasx)
coordenadasy = input('Informe a coordenada de y: ')
coordenadasy = int(coordenadasy)

if (coordenadasx >= 1 and coordenadasy >= 1):
    print(f'quadrante 1: x: {coordenadasx} e y: {coordenadasy}')
elif (coordenadasx <= -1 and coordenadasy >= 1):
    print(f'quadrante 2: x: {coordenadasx} e y: {coordenadasy}')
elif (coordenadasx <= -1 and coordenadasy <= -1):
    print(f'quadrante 3: x: {coordenadasx} e y: {coordenadasy}')
elif (coordenadasx >= 1 and coordenadasy <= -1):
    print(f'quadrante 1: x: {coordenadasx} e y: {coordenadasy}')
else:
    print('Formato incorreto.')