a, b, c = 0, 0, 0
p = 120

# Perímetro do 🔺 retângulo
# |-------------------------------|
# 0              60              120 perimetro
# a <= b < c. Considere c como hipotenusa - lado maior

for a in (1, p // 2):
    for b in (1, (p - a) // 2 + 1):
        c = p - a - b
    if a * a + b * b == c * c:
        print(a, b, c)