lista = [1]
print(lista)

n = 1
while n < 25:
    lista1 = [1]
    for posicao in range(len(lista) - 1):
        lista1.append((lista[posicao] + lista[posicao + 1]))
    
    lista1.append(1)
    print(lista1)
    lista = lista1
    n += 1


elemento = 1307504
