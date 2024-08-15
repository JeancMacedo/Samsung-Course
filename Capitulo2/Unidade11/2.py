#USO DE .FORMAT
print('Números reais com 10 caracteres: {0:10.3f}, {0:10.4f}'.format(3.1415926))

for i in range(2, 11, 2):
    print('{0:3d} {1:4d} {2:5d} {3:6d}'.format(i, i*i, i*i*i, i*i*i*i))
#{0: para o item de dentro do .format, :3d quantidade de espaços que utiliza}
"""
na prática,
por exemplo '{0:3d}'.format(i)
vai utilizar o conteudo do i, no 0:,
e no 3d, é quantidade casas que utiliza
resultado exemplo: 
  0
"""