breads = ["Pão de centeio", 'trigo', 'Branco']
meats = ["Almôdega","Salsicha","Peito de frango"]
vegis = ["Alface","Tomate","Pepino"]
sauces = ["Maionese"," Mostarda e mel","Pimenta"]

print("Possiveis combinações de sanduíche do Usuario")
for b in breads:
    for m in meats:
        for v in vegis:
            for s in sauces:
                print(b, " + " , m, " + " , v, " + ", s)