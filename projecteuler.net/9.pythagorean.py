# conjunto de três números a < b < c
# a² + b² = c²

a, b, c = 0, 0, 0
produto = 0
soma = 1000

for a in range(1, soma // 3):
    for b in range(a + 1, soma // 2):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            produto = a * b * c
            break
    if produto > 0:
        break

print(f"Trigêmeo pitagórico: (a, b, c) = ({a}, {b}, {c})")
print(f"Produto abc = {produto}")