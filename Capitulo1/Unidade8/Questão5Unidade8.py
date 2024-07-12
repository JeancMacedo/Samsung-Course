def generate_snake(n):
    num = 1
    for i in range(n):
        if i % 2 == 0:
            for j in range(1, n+1):
                print(num, end="\t")
                num += 1
        else:
            for j in range(n, 0, -1):
                print(num, end="\t")
                num += 1
        print()

# Leitura do valor de n
n = int(input("Digite o valor de n: "))
generate_snake(n)


#FAZER SOZINHO, ESSE DAI TIREI DO CHATGPT