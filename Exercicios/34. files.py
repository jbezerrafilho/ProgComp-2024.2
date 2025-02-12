horas = {}
minutos = {}

fd = open('log.txt', 'r')

for linha in fd:
    posI = linha.find('[')
    posF = linha.find(']')
    print(linha[posI + 1:posF])
fd.close()

# linha = fd.readline()
# while linha != "":
#     posI = linha.find('[')
#     posF = linha.find(']')
#     print(linha[posI + 1:posF])
#     linha = fd.readline()
# fd.close()