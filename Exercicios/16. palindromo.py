print("Digite um numero de 03 digitos? ")
numero =  int(input())

a = numero % 10
numero = numero // 10

b = numero // 10


if a == b :
    print("palíndromo")
else: 
    print("Não é palíndromo!!")
