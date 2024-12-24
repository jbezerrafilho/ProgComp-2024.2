# Definindo o limite superior para o perímetro
limite = 120

# Inicializando variáveis para armazenar o melhor resultado
melhor_p = 0
max_solucoes = 0

# Loop pelos valores possíveis de p
for p in range(1, limite + 1):
    contador = 0  # Contador de soluções para o valor atual de p
    
    # Testando possíveis valores de a e b
    for a in range(1, p // 2):
        for b in range(a, (p - a) // 2 + 1):
            c = p - a - b  # Calculando c
            if a * a + b * b == c * c:  # Verificando se é um triângulo retângulo
                contador += 1
                print(a, b, c)
    # Atualizando o valor máximo de soluções
    if contador > max_solucoes:
        max_solucoes = contador
        melhor_p = p

# Exibindo o resultado
print(f"O valor de p com o maior número de soluções é {melhor_p}, com {max_solucoes} soluções.")