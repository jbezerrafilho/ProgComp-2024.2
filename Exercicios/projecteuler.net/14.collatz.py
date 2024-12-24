# Developed by J. Bezerra
# November / 2024
# https://projecteuler.net/problem=14 

num = int(input("Digite um número para ver a sequência de Collatz: "))
n = 1

#Tamanho da sequência
maior_sequencia = -50
#Número que gerou a maior sequência
num_maior_sequencia = -50

#Calculando as sequências de 1 até o número digitado pelo usuário
while n <= num:

    #Calculando a sequência de um número n
    numero = n
    qtd_termos = 1
    while numero != 1:
        
        if numero % 2 == 0:
            numero = int(numero / 2)
        else:
            numero = 3 * numero + 1
        qtd_termos += 1
        
    #Definindo a maior sequencia e o número que gerou
    if qtd_termos > maior_sequencia:
        maior_sequencia = qtd_termos
        num_maior_sequencia = n
    n += 1

print(f'A maior sequência tem {maior_sequencia} termos e \
foi gerada pelo número {num_maior_sequencia}')


