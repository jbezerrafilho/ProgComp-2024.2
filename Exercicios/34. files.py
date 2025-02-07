from pprint import pprint  
horas = {}
minutos = {}

with open('log.txt', 'r') as file:
    for line in file:
        #print(line)
        w = line.split()
        data = w[3][1:].split(':')
        horas[data[1]] = horas.get(data[1], 1) + 1
        minutos[data[2]] = minutos.get(data[2], 1) + 1

pprint(minutos)