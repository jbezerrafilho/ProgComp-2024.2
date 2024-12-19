#import random
#lista_temp = [random.randint(1, 100) for n in range(5)]

lista = [5, 8 , 12, 7, 25, 43]
lista1 = [1]

for i in range(len(lista) - 1):
    lista1.append((lista[i] + lista[i + 1]))

lista1.append(1)

print(lista1)