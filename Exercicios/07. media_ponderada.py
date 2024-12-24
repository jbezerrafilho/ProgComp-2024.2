""""
O professor da disciplina fez um trabalho e uma prova para cada uma das
unidades. Para obter a nota de cada unidade, o trabalho tinha peso de 30% e a
prova de 70%. Segundo os critérios do IFRN, a nota na disciplina é formada pela
nota da primeira unidade (com peso 40%) e a nota da segunda unidade (com peso
60%); passa por média quem obtiver 6,0 ou mais.
Dadas as notas: t1 (primeiro trabalho), p1 (primeira prova) e t2 (segundo
trabalho), calcule a nota a obter na segunda prova para passar por média.
"""

MSG = "Digite a nota "
t1 = float(input(MSG + 't1: '))
p1 = float(input(MSG + 'p1: '))
t2 = float(input(MSG + 't2: '))
#p2 = ?

#Calculando a média ponderada das unidades
nota_unidade1 = (t1 * 0.3) + (p1 * 0.7)
# nota_unidade2 = (t2 * 0.3) + (p2 * 0.7)


# Calculando a média da disciplina
# Média para passar:
# 6.00 = (nota_unidade1 * 0.4) + (nota_unidade2 * 0.6)
nota_unidade2 = (6.00 - (nota_unidade1 * 0.4)) / 0.6
p2 = round(((nota_unidade2 - (t2 * 0.3))/ 0.7), 2)
print('A nota da prova 2 terá que ser: ', p2)