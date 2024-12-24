try:
    print("Digite um número de três dígitos: ")
    num = int(input())

    digito_unidade = num % 10
    num = num // 10

    digito_dezena = num % 10
    num = num // 10

    digito_centena = num % 10
    num = num // 10

    #Invertendo o número armazenado na variável num
    num = num * 10 + digito_unidade
    num = num * 10 + digito_dezena
    num = num * 10 + digito_centena

    print(f'O número que foi digitado ao ser invertido será: {num}')

except ValueError as error:
    print('Digite um valor númerico de três dígitos!')
    print(error)