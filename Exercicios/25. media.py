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

for num in numeros:
    desvio_padrao += (num - media) ** 2
desvio_padrao = (desvio_padrao / (contador - 1)) ** 0.5

print(desvio_padrao)