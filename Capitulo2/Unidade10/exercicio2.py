prime_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_list.append(11)

for num in prime_list:
    if num > 1:  # Todos os números primos são maiores que 1
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(f"{num} é um número primo")

