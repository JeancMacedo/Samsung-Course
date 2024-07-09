print("True para centésimo digito = 3, False para qualquer outro digito que não seja 3 na casa centesima.", end= "\n\n")
def centésimo_dígito(numero):
    # Converte o número para string para acessar os dígitos
    numero_str = str(numero)

    # Verifica se o número tem exatamente 3 dígitos
    if len(numero_str) == 3:
        # Verifica se o centésimo dígito é 3
        if numero_str[0] == '3':
            return True
        else:
            return False
        
    else:
        return False
    
# Recebe um número inteiro de 3 dígitos do usuário
numero = int(input("Digite um número inteiro de 3 dígitos: "))

# Chama a função e imprime o resultado
resultado = centésimo_dígito(numero)
print(resultado)