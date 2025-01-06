# Developed by J.Bezerra 
# Janeiro de 2025

# Atenção: O código finalizaou em aproximadamente 12s.
limite = 1000000
contador = 0
primo_anterior = 0
primo_atual = 0

dividendo = 3
while dividendo <= limite:

    # Divisor
    div = 2
    eh_primo = True
    while div <= (dividendo**(1/2)):
        if dividendo % div == 0:
            eh_primo = False
            break
        div += 1

    # Se for primo atualize as variáveis
    if eh_primo:
        primo_anterior = primo_atual
        primo_atual = dividendo
        # Se for um par de números primos ímpares e consecutivos, incremente o contador
        if (primo_atual - primo_anterior) == 2:
            contador += 1
            # Caso queira visualizar os pares consecutivos, tire o comentário a seguir
            #print( f'({primo_anterior}, {primo_atual})')

    dividendo += 1


print(f'A soma dos pares primos (ímpares consecutivos) menores que {limite} \
é {contador} pares.')
