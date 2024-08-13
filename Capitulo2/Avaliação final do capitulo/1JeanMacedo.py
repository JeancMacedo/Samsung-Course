# Definindo as strings s1 e s2
s1 = ["Eu amo", "Eu gosto de"]
s2 = ["Panqueca", "Suco de laranja", "Café"]

# Usando laços para imprimir os resultados desejados
for frase in s1:
    for item in s2:
        print(f"{frase} {item}.")