def processar_notas(notas):
    # O número total de alunos é o tamanho da lista dividido por 3
    total_alunos = len(notas) // 3
    
    # Inicializar variáveis para contar alunos com todas as notas válidas
    alunos_validos = []
    
    # Processar cada aluno
    for i in range(total_alunos):
        # Extrair as notas de um aluno (três notas consecutivas)
        aluno_notas = notas[i*3:(i+1)*3]
        
        # Verificar se o aluno tem todas as notas válidas (sem 0)
        if 0 not in aluno_notas:
            alunos_validos.append(aluno_notas)
    
    # Número de alunos com notas válidas
    num_alunos_validos = len(alunos_validos)
    
    # Exibição dos resultados
    print(f'notas = {notas}')
    print(f'O número total de alunos é {total_alunos}.')
    print(f'O número de alunos com notas válidas é {num_alunos_validos}:')
    print(alunos_validos)

# Exemplo de entrada
notas = [100, 90, 95, 90, 80, 70, 0, 80, 90, 90, 0, 90, 100, 75, 20, 30, 50, 90]

# Processando as notas
processar_notas(notas)