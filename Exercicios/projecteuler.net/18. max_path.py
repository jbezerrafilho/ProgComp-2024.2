caminhos = [
 [3],
 [7, 4],
 [2, 4, 6],
 [8, 5, 9, 3]
 ]

temp = [3]

for l in range(1, len(caminhos)):
    caminhos[l][0] += caminhos[l-1][0] # Primeiro elemento
    for c in range(1, len(caminhos[l])-1): # Elementos do meio
        caminhos[l][c] += max(caminhos[l-1][c-1], caminhos[l-1][c])
    caminhos[l][l] += caminhos[l-1][l-1] # Ultimo elemento
    temp.append(max(caminhos[l]))   
    
# caminhos[-1] é a ultima linha da matriz ou último elemento de uma lista
# Equivalente a caminhos[len(caminhos)-1]
print(max(caminhos[-1])) 
print(temp)

