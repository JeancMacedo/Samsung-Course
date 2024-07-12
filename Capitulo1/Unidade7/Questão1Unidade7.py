letra = input('Informe uma letra e veja se é uma vogal: ')
#letra = str(letra)

if(letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u'):
    print(f"\na letra {letra} é uma vogal!")
elif(letra != 'a' and letra != 'e' and letra != 'i' and letra != 'o' and letra != 'u' ):
    print(f"\na letra {letra} é uma consoante!")
