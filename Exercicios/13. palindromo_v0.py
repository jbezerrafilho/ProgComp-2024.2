# Este código verifica se o número de 3 dígitos é palíndromo

try:
    num = int(input("Digite um número:? "))

    msg = "é um palíndromo!"
    if num // 100 != num % 10:
        print(num, "não", msg)
    else:
        print(num, msg)

except ValueError as error:
    print("Digite um número válido!")
