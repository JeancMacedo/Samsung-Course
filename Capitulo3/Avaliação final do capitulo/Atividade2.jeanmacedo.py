def verificar_palindromo(texto):
    # Caso base: se o texto tem 0 ou 1 caractere, é um palíndromo
    if len(texto) <= 1:
        return True
    # Verifica se o primeiro e o último caractere são iguais
    if texto[0] == texto[-1]:
        # Chama a função recursivamente, removendo o primeiro e o último caractere
        return verificar_palindromo(texto[1:-1])
    # Se o primeiro e o último caractere não forem iguais, não é um palíndromo
    return False

# Recebe a string do usuário
texto = input("Digite uma palavra ou frase: ").replace(" ", "").lower()

# Verifica se é um palíndromo
if verificar_palindromo(texto):
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")
