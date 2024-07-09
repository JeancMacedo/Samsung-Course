""" 
"Vá direto para o oeste neste cruzamento". 
Você verá quatro edifícios. 
Quando vir os correios, vire à direita do outro 
lado da estação dos correios. 
Vá direto, e quando você ver um restaurante italiano,
o terceiro edifício é o hotel que você está procurando". 

"""
print("Vá direto para o oeste neste cruzamento!")
print("\nVocê verá quatro edifícios!")
edificio = input("\nVocê foi direto para oeste por esse cruzamento \
e viu quatro edifícios?")
while edificio == 'sim' or edificio == "Sim" or edificio == "SIM": 
    print('\nAgora, quando vir os correios, vire à direita do outro \
lado da estação dos correios')
    break
else:
    print('*******************************************************')
    print('Volte ao inicio e siga o procedimento correto!')
    print('*******************************************************')

correios = input("\nApós virar a direita e ir direto \
você vê um restaurante italiano? ")
while correios == 'sim' or correios == "Sim" or correios == "SIM": 
    print('\nCerto, o terceiro edifício é o hotel que você está \
procurando!')
    break
else:
    print('*******************************************************')
    print('Volte a etapa anterior e siga o procedimento \
correto!')
    print('*******************************************************')



    