primo = int((input('Digite um número para ver se é primo: ')))

i = 1
ndiv = 0

while i <= primo:
	if primo % i == 0:
		ndiv = ndiv + 1
	i = i + 1

if ndiv == 2:
	print("É primo!!")
else:
	print("Não é primo! Tem ", ndiv, "divisores.")