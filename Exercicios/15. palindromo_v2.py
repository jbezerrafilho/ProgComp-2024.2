# Este código verifica se o número de 3 dígitos é palíndromo
# Código mais otimizado para realizar o palíndromo de mais
# de 03 dígitos

try:
    num = int(input("Digite um número:? "))
    direto = num
    inverso = 0

    #Observe a repetição...
    digito = num % 10
    inverso = inverso * 10 + digito
    num //= 10

    digito = num % 10
    inverso = inverso * 10 + digito
    num //= 10
    
    digito = num % 10
    inverso = inverso * 10 + digito
    num //= 10


    msg = " "
    if direto != inverso:
        msg = "não"
    print(direto, msg, "é palíndromo!")
    

except ValueError as error:
    print("Digite um número válido!")
