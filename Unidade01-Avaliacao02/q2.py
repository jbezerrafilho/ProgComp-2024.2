# Developed by J.Bezerra 
# Dezembro de 2024

num_inicial = 10
num_final = 100000
contador = 0
msg = f'No intervalo de {num_inicial} a {num_final}'

# Este laço repete 'alguma coisa' dentro do intervalo que
# vai do número inicial até o número final dado no problema
while num_inicial <= num_final:
  
    direto = num_inicial
    num_temp = num_inicial
    inverso = 0

    # Repita algo enquanto a variável > 0
    while num_temp > 0: 
        # Pegamos cada dígito do numero
        digito = num_temp % 10
        # E invertemos...
        inverso = inverso * 10 + digito
        # Diminuimos a gandeza da variável temp
        num_temp = num_temp // 10

    # Verificando se o número é palíndromo    
    if direto == inverso:
        contador += 1
    # Importante incrementar a variável de controle para o while externo não ficar em loop 
    num_inicial += 1

print(f'{msg} temos {contador} números palíndromos')