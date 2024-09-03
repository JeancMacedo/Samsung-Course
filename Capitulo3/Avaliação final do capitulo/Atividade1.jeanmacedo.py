import math

# Recebe as coordenadas dos dois pontos
x1, y1 = map(float, input("Digite as coordenadas do primeiro ponto (x1 y1): ").split())
x2, y2 = map(float, input("Digite as coordenadas do segundo ponto (x2 y2): ").split())

# Calcula a distância entre os dois pontos usando a fórmula de distância
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Imprime a distância
print(f"A distância entre os pontos é: {distancia:.2f}")