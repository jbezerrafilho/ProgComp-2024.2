triangulo = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 0, 70, 98, 73, 93, 38, 53, 60, 0, 23]
]

# Copiar o triângulo original para um auxiliar 
triangulo_aux = []
for row in triangulo:
    triangulo_aux.append(row[0: len(row)])

# Cálculo da soma máxima de baixo para cima no triângulo auxiliar
for i in range(len(triangulo_aux) - 2, -1, -1):  # Começa na penúltima linha
    for j in range(len(triangulo_aux[i])):
        # Adicionar o máximo dos dois possíveis caminhos abaixo
        triangulo_aux[i][j] += max(triangulo_aux[i + 1][j], triangulo_aux[i + 1][j + 1])

# Reconstruir o caminho para soma máxima
path_to_max_sum = []

# O 'i' percorre as linhas do triângulo e o 'j' percorre as colunas(elementos dentro da linha)
# Só que do topo para baixo
j = 0  
for i in range(len(triangulo) - 1):
    path_to_max_sum.append(triangulo[i][j])
    if triangulo_aux[i + 1][j] < triangulo_aux[i + 1][j + 1]:
        j += 1
# Adiciona o último elemento do caminho      
path_to_max_sum.append(triangulo[len(triangulo) - 1][j])

print("Maior soma:", triangulo_aux[0][0])
print("Caminho para soma máxima:", path_to_max_sum)