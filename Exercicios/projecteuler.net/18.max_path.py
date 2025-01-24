triangle = [
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

# Copiar o triângulo original para manter a matriz de somas
# triangle_copy = [row[:] for row in triangle]
triangle_copy = []
for row in triangle:
    triangle_copy.append(row[0: len(row)])

# Cálculo da soma máxima de baixo para cima
for i in range(len(triangle) - 2, -1, -1):  # Começa na penúltima linha
    for j in range(len(triangle[i])):
        # Adicionar o máximo dos dois possíveis caminhos abaixo
        if triangle_copy[i + 1][j] > triangle_copy[i + 1][j + 1]:
            triangle_copy[i][j] += triangle_copy[i + 1][j]
        else:
            triangle_copy[i][j] += triangle_copy[i + 1][j + 1]

# Reconstruir o caminho para soma máxima
path_to_max_sum = []
j = 0  # Inicia no topo do triângulo
for i in range(len(triangle) - 1):
    path_to_max_sum.append(triangle[i][j])
    if triangle_copy[i + 1][j] < triangle_copy[i + 1][j + 1]:
        j += 1
path_to_max_sum.append(triangle[-1][j])

# Resultado
print("Maior soma:", triangle_copy[0][0])
print("Caminho para soma máxima:", path_to_max_sum)