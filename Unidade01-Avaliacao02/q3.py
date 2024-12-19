
num = int((input('Digite um número para ver quantos primos existe entre 3 e ele: ')))
contador = 0
primo_anterior = 0
primo_atual = 0

i = 3
while i <= num:   
    # Esta laço interno testa se 'i'é primo
    # 'j' representa os possíveis divisores de 'i' 
    #Comecei com 2, pois todo número é divisível por 1
    #Por isso ndiv já começa com 1 divisor
    j = 2     
    ndiv = 1  
    while j <= i:
        if i % j == 0:
            ndiv += 1
        j += 1

    #Validamos se o 'i' é primo e incrementamos 'qtd_primos'    
    if ndiv == 2:
        primo_atual = i
    i += 2

print(f'A soma de primos no intervalo até {num} \
é {contador}.')

