lista = [1]
print(lista)

n = 1
while n < 6:
    temp = [1]
    for pos in range(len(lista) - 1):
        temp.append((lista[pos] + lista[pos + 1]))
    
    temp.append(1)
    print(temp)
    lista = temp
    n += 1


#elemento = 1307504
