limite = 100000
contador = 0
primo_anterior = 0
primo_atual = 0

dividendo = 3
while dividendo <= limite:

    # Divisor
    div = 2
    # Número de divisores
    ndiv = 1  
    while div <= dividendo:
        if dividendo % div == 0:
            ndiv += 1
        div += 1

    # Se for primo atualize as variáveis
    if ndiv == 2:
        primo_anterior = primo_atual
        primo_atual = dividendo
        if (primo_atual - primo_anterior) == 2:
            contador += 1
            print( f'({primo_anterior}, {primo_atual})')

    dividendo += 1


print(f'A soma dos pares primos (ímpares consecutivos) menores que {limite} \
é {contador} pares.')
