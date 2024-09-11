def bin1(n, k):
    B = [0] * (n + 1)
    for i in range(n + 1):
        for j in range (n - 1, -1):
            if j == 0 or j == i:
                B[j] = 1
            else:
                B[j] = n[j] + B[j - 1]
    return B[k]
for i in range(10):
    for j in range(i + 1):
        print(bin1(i, j), end=' ')
    print()
print("Espaço " * 5)
print()
def bin2(n, k):
    B = [0] * (n + 1)
    for i in range(n + 1):
        for j in range (n - 1, -1):
            if j == 0 or j == i:
                B[j] = 1
            else:
                B[j] = n[j] + B[j - 1]
    return B[k]
for i in range(10):
    for j in range(i + 1):
        print(bin2(i, j), end=' ')
    print()
print("Espaço " * 5)
print()

def bin3(n, k):
    B = [0] * (n + 1)
    for i in range(n + 1):
        for j in range (n - 1, -1):
            if j == 0 or j == i:
                B[j] = 1
            else:
                B[j] = n[j] + B[j - 1]
    return B[k]
for i in range(10):
    for j in range(i + 1):
        print(bin3(i, j), end=' ')
    print()