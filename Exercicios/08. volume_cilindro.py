"""
Dados, o raio e a altura, desenvolva um programa que calcula o volume de um
cilindro.
"""

PI = 3.14159
raio = int(input('Digite o raio da base do cilindro: '))
altura = int(input('Digite a altura do cilindro: '))
volume = round((PI * (raio ** 2) * altura), 2)

print(f'O volumde do cilindro de raio {raio} e ' 
      f'altura {altura} é {volume}')


#José Bezerra
#Nov/2024