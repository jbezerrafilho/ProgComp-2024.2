num_inicial = 10
num_final = 987631
contador = 0

# Este laço repete 'alguma coisa' dentro do intervalo que
# vai do número inicial até o número final dado no problema
while num_inicial <= num_final:

    # num_temp é uma variável temporária para ser manipulada no laço interno
    # onde manipularmeos os digitos do número
    num_temp = num_inicial


    eh_decrescente = True

    # Este laço valida se um número é descrescente
    while eh_decrescente and num_temp >= 10:

        # lsd -> Least Significant Digit (Dígito menos signicativo)
        lsd = num_temp % 10
        num_temp = num_temp // 10

        # msd -> Most Significant Digit (Dígito mais signifiativo)
        msd = num_temp % 10

        if lsd > msd:
            eh_decrescente = False
            # Essa variável como 'False' interrompe o laço interno

    if eh_decrescente:
        contador += 1
    # Importante incrementar a variável de controle para o while externo não ficar em loop
    num_inicial += 1

print(f'No intervalo de 10 a 987631 \
temos {contador} números decrescentes')