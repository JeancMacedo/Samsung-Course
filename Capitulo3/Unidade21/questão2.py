class Dog:
    def __init__(self, name):
        # Inicializa o atributo nome
        self.name = name

    def bark(self):
        # Imprime o som de latido com o nome do cão
        print(f"{self.name} : woof woof")

# Criar uma instância da classe Dog com o nome 'Bingo'
my_dog = Dog('Bingo')

# Chamar o método bark para imprimir o som de latido
my_dog.bark()
