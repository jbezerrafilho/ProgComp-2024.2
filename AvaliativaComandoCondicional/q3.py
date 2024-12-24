# Developed by J.Bezerra e Eduarda
# Novembro de 2024

import random

try:
    numero_sorteado = random.randint(1, 100)
    
    # Definindo início do intervalo
    inicio = 1
    fim = 100

    # Valida se o usuário acertou a tentativa
    right = False

    # Incrementa a quantidade de tentativas
    qtd_tentativas = 0
    
    
    # Tentativa 1
    if not right:
        msg = f'Qual o número sorteado no intervalo de {inicio} a {fim}? '
        tentativa = int(input(msg))
        qtd_tentativas += 1
        if tentativa == numero_sorteado:
            print(f'Você acertou! O número secreto é {numero_sorteado}!')
            right = True
        elif tentativa < numero_sorteado:
            inicio = tentativa + 1
        elif tentativa > numero_sorteado:
            fim = tentativa - 1

    # Tentativa 2
    if not right:
        msg = f'Qual o número sorteado no intervalo de {inicio} a {fim}? '
        tentativa = int(input(msg))
        qtd_tentativas += 1
        if tentativa == numero_sorteado:
            print(f'Você acertou! O número secreto é {numero_sorteado}!')
            right = True
        elif tentativa < numero_sorteado:
            inicio = tentativa + 1
        elif tentativa > numero_sorteado:
            fim = tentativa - 1

    # Tentativa 3    
    if not right:
        msg = f'Qual o número sorteado no intervalo de {inicio} a {fim}? '
        tentativa = int(input(msg))
        qtd_tentativas += 1
        if tentativa == numero_sorteado:
            print(f'Você acertou! O número secreto é {numero_sorteado}!')
            right = True
        elif tentativa < numero_sorteado:
            inicio = tentativa + 1
        elif tentativa > numero_sorteado:
            fim = tentativa - 1

    # Tentativa 4    
    if not right:
        msg = f'Qual o número sorteado no intervalo de {inicio} a {fim}? '
        tentativa = int(input(msg))
        qtd_tentativas += 1
        if tentativa == numero_sorteado:
            print(f'Você acertou! O número secreto é {numero_sorteado}!')
            right = True
        elif tentativa < numero_sorteado:
            inicio = tentativa + 1
        elif tentativa > numero_sorteado:
            fim = tentativa - 1

    # Valida o término das tentativas       
    if qtd_tentativas == 4:
        print('Tentativas esgotadas!')
        
except ValueError as e:
    print(e)
    print('Digite um número válido!')