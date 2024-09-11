def encontrar_moeda_pesada(moedas):
    grupo1 = moedas[:3]
    grupo2 = moedas[3:6]
    grupo3 = moedas[6:]


    def balanca(grupoA, grupoB):
        pesoA = sum(moeda[1] for moeda in grupoA) 
        pesoB = sum(moeda[1] for moeda in grupoB)  
        if pesoA > pesoB:
            return 'A'
        elif pesoB > pesoA:
            return 'B'
        else:
            return 'igual'

    resultado1 = balanca(grupo1, grupo2)

    if resultado1 == 'igual':
        grupo_pesado = grupo3
    elif resultado1 == 'A':
        grupo_pesado = grupo1
    else:
        grupo_pesado = grupo2

    resultado2 = balanca([grupo_pesado[0]], [grupo_pesado[1]])

    if resultado2 == 'igual':
        moeda_pesada = grupo_pesado[2]
    elif resultado2 == 'A':
        moeda_pesada = grupo_pesado[0]
    else:
        moeda_pesada = grupo_pesado[1]

    return moeda_pesada[0]  
moedas = [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 2)]  # Moeda 9 é mais pesada

moeda_pesada = encontrar_moeda_pesada(moedas)
print(f"A moeda pesada é a {moeda_pesada}")
