Autor: José Bezerra
import math

"""
Calcule o tempo de uma dívida aplicado à juros compostos.
Fórmula para cálculo M = C * (1 + i) ** t , onde:
    M = Montante, C = Capital, i = taxa, t = tempo. 
"""
capital = float(input('Qual o valor da dívida? '))
montante = float(input('Valor do montante? '))
taxa = float(input('Valor da taxa? ')) / 100

#Isolando t na fórmula de juros compostos, teremos:
tempo = int(math.ceil(((math.log(montante/capital)/math.log(1 + taxa)))))

print('O tempo será de', tempo, 'meses.')
