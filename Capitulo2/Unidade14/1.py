print("Iniciar programa de cardápio do café... Pressione 'q' para sair")
cafe_menu = {'Café gelado' : 3000}

while True:
    str = input('$ ')
    if str.startswith('q'):
        break;
    command = str[0]

    if command == '<':
        str = str.replace('<', "")
        inputStr = str.split(':')
        if len(inputStr) < 2 :
            print('input error')
            continue
        else:
            cafe_menu[inputStr[0].strip()] = inputStr[1].strip()

    elif command == '>':
        str = str.replace('>',"")
        inputStr = str.strip()
        if inputStr in cafe_menu:
            print(cafe_menu[inputStr])
        else:
            print('{} não está no cardápio.'.format(inputStr))
    elif command == 'q':
        break
    else:
        print('input error.')
print("Saindo do programa de cardápio do café.")