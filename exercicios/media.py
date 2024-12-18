numeros = []
soma = 0
contador  = 0
num = float(input("Digite um número: "))

while num >= 0:
    soma += num
    contador += 1
    numeros.append(num)
    num = float(input("Digite um número: "))
if contador > 0:
    print(soma / contador)
else:
    print("Média não existe!")

media = soma / contador
desvio_padrao = 0

for i in numeros:
    
