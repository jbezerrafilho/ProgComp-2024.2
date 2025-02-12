def d(n):
    sum = 0
    for i in range(1, (n//2 +1)):
        if n % i == 0:
            sum += i
    return sum

soma = 0
for a in range(2, 10001):
    b = d(a)
    if d(b) == a and a != b:
        soma += a  
        #soma += b

print(soma)

# def soma_divisores(n):
#     """Retorna a soma dos divisores próprios de n (excluindo n)."""
#     soma = 1  # 1 é sempre um divisor próprio
#     for i in range(2, int(n**0.5) + 1):  # Itera até a raiz quadrada de n
#         if n % i == 0:
#             soma += i
#             if i != n // i:  # Evita contar o mesmo divisor duas vezes
#                 soma += n // i
#     return soma

# def numeros_amigos(limite):
#     """Encontra a soma de todos os números amigos abaixo de 'limite'."""
#     soma_total = 0
#     for a in range(2, limite):
#         b = soma_divisores(a)
#         if b != a and soma_divisores(b) == a:  # Confirma se são amigos
#             soma_total += a
#     return soma_total

# # Define o limite como 10.000 e exibe o resultado
# limite = 10000
# resultado = numeros_amigos(limite)
# print(f"A soma de todos os números amigos abaixo de {limite} é: {resultado}")