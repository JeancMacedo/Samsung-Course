idade = input("Informe sua idade: ")
idade = int(idade)

if (idade >= 20 and idade <= 59):
    print(f'Idade = {idade}, você é da classe Adulto.')
elif (idade < 20 and idade >= 10):
    print(f'Idade = {idade}, você é da classe Jovem.')
elif (idade >=1 and idade < 10):
    print(f'Idade: {idade}, você é da classe Criança.')
elif (idade >= 60):
    print(f'Idade: {idade}, você é da classe Idoso.')
else:
    print("Informe uma idade possivel.")
