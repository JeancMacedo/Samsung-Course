print('Bem vindo ao park de diversões!\n\n')
idade = input("Informe sua idade: ")
idade = int(idade)
print('\n Informar sua altura no formato float (ex: 1.51)')
altura = input("\nInforme sua altura: ")
altura = float(altura)

if ( idade >= 16 and altura >= 1.50):
    print("Você pode entrar.")
else:
    print("Você não pode entrar.")