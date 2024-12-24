num = int((input('Digite um número para ver quantos primos existe entre 2 e ele: ')))
qtd_primos = 0

i = 2
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
        qtd_primos += 1
    i += 1
print(f'A quantidade de primos no intervalo até {num} \
é de {qtd_primos} número(s).')
