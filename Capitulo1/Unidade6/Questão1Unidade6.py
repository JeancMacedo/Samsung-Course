pontuacaoUsuario = input("Informe a pontuação do usuario: ")
pontuacaoUsuario = int(pontuacaoUsuario)

if (pontuacaoUsuario >= 1000):
    print('Você é um(a) mestre(a).')
elif (pontuacaoUsuario <= 1000 and pontuacaoUsuario > 0):
    print("Você é um(a) novato(a).")
else:
    print("Você tem 0 pontos, sem menções ainda.!")
