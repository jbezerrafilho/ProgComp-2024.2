# Este código verifica se o número de 3 dígitos é palíndromo

try:
    num = int(input("Digite um número:? "))
    num_original = num

    digito1 = num % 10
    num //= 10

    digito2 = num % 10
    num //= 10

    #Expressão desnecessária, mas será mantida para 
    #preservar o bom entendimento
    digito3 = num % 10
    num //= 10

    inverso = 0
    inverso = inverso * 10 + digito1
    inverso = inverso * 10 + digito2
    inverso = inverso * 10 + digito3

    msg = "é um palíndromo!"
    if num_original != inverso:
        print(num_original, "não", msg)
    else:
        print(num_original, msg)

except ValueError as error:
    print("Digite um número válido!")
