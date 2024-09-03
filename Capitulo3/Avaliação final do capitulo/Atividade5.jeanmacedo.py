class Vetor:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __mul__(self, other):
        return Vetor(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        return Vetor(self.x / other.x, self.y / other.y)

    def __repr__(self):
        return f"({self.x}, {self.y})"

v1, v2 = Vetor(30, 40), Vetor(10, 20)
print(f"v1 * v2 = {v1 * v2}")
print(f"v1 / v2 = {v1 / v2}")
