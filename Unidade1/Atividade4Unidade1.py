print("""Hello
World!""")

print('''Hello\
World!''')

try:
    a, b = input("Insira dois números inteiros: ").split()
    result = int(a) / int(b)
    print('{}/{} = {}'.format(a, b, result))
except:
    print("Verifique se os números inteiros foram inseridos corretamente")