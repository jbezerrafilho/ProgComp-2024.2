
num_inicial = 10
num_final = 987631
contador = 0

# Este laço repete 'alguma coisa' dentro do intervalo que
# vai do número inicial até o número final dado no problema
while num_inicial <= num_final:
    #num_temp é uma variável temporária para ser manipulada no laço interno
    #onde manipularmeos os digitos do número
    num_temp = num_inicial

    # Comecei errando o lugar desta variável colocando-a fora do while externo
    # Quando o número não era decrescente, por estar fora do laço, não tinha como
    # resetá-la para true. Percebi e a coloquei no lugar correto
    eh_decrescente = True

    # Esta laço verifica se um número específico é descrescente 
    while eh_decrescente and num_temp >= 10: 

        # lsd -> Least Significant Digit (Dígito menos signicativo)
        lsd = num_temp % 10
        num_temp = num_temp // 10

        # msd -> Most Significant Digit (Dígito mais signifiativo)
        msd = num_temp % 10

        if lsd > msd:
            eh_decrescente = False
        # Saindo do laço interno

    if eh_decrescente:
        contador += 1
    # Importante incrementar a variável de controle para o while externo não ficar em loop 
    num_inicial += 1

# Galileu, perdoe o excesso de comentários. Fica mais fácil o entendimento
print(f'No intervalo de 10 a 987631 \
temos {contador} númeoros decrescentes')