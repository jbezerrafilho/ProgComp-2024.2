caminhos = [
 [75],
 [95, 64],
 [17, 47, 82],
 [18, 35, 87, 10],
 [20,  4, 82, 47, 65],
 [19,  1, 23, 75,  3, 34],
 [88,  2, 77, 73,  7, 63, 67],
 [99, 65,  4, 28,  6, 16, 70, 92],
 [41, 41, 26, 56, 83, 40, 80, 70, 33],
 [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
 [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
 [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
 [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
 [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
 [ 4, 62, 98, 27, 23,  0, 70, 98, 73, 93, 38, 53, 60,  0, 23]
]

# Caminho para chegar no maior valor
path_to_max_sum = [75]


for l in range(1, len(caminhos)):
    caminhos[l][0] += caminhos[l-1][0] # Primeiro elemento
    for c in range(1, len(caminhos[l])-1): # Elementos do meio
        caminhos[l][c] += max(caminhos[l-1][c-1], caminhos[l-1][c])
    caminhos[l][l] += caminhos[l-1][l-1] # Ultimo elemento
    path_to_max_sum.append(max(caminhos[l]) -  max(caminhos[l-1]) )   

# caminhos[-1] é a ultima linha da matriz ou último elemento de uma lista
# Equivalente a caminhos[len(caminhos)-1]
print(max(caminhos[-1])) 
print(path_to_max_sum)

