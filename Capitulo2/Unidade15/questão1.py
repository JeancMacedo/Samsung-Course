student_tuple = [('211101','David Doe', 
                   '010-123-1111'),
                ('211102', 'John Smith', 
                   '010-123-2222'), 
                ('211103', 'Jane Carter', 
                   '010-123-3333')]

num = input("Informe o número de identificação: ")

# Verificação se o num existe dentro de uma das tuplas
for student in student_tuple:
    if num == student[0]:  # Comparando com o primeiro item da tupla (ID)
        print(f"O aluno {num} é {student[1]} tem o número de telefone {student[2]}")
        break
else:
    print("Número de identificação não encontrado.")