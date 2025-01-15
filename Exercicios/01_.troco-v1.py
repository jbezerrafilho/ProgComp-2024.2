conta = int(input('Qual o valor da conta? '))
pago = int(input('Quanto o cliente pagou? '))
troco = pago - conta
troco_variavel = troco

# Denominações de moedas
c200, c100, c50, c20, c10, c5, c2, m1 = 0, 0, 0, 0, 0, 0, 0, 0

for t in [200, 100, 50, 20, 10, 5, 2, 1]:
    if troco_variavel >= 200:
        c200 = troco_variavel // 200
        troco_variavel = troco_variavel % 200
    elif troco_variavel >= 100:
        c100 = troco_variavel // 100
        troco_variavel = troco_variavel % 100
    elif troco_variavel >= 50:
        c50 = troco_variavel // 50
        troco_variavel = troco_variavel % 50
    elif troco_variavel >= 20:
        c20 = troco_variavel // 20
        troco_variavel = troco_variavel % 20
    elif troco_variavel >= 10:
        c10 = troco_variavel // 10
        troco_variavel = troco_variavel % 10
    elif troco_variavel >= 5:
        c5 = troco_variavel // 5
        troco_variavel = troco_variavel % 5
    elif troco_variavel >= 2:
        c2 = troco_variavel // 2
        troco_variavel = troco_variavel % 2
    else:
        m1 = troco_variavel


print()
print("Troco: R$", troco)
print()
print("Cédula R$ 200:", c200)
print("Cédula R$ 100:", c100)
print("Cédula R$ 50: ", c50)
print("Cédula R$ 20: ", c20)
print("Cédula R$ 10: ", c10)
print("Cédula R$ 5:  ", c5)
print("Cédula R$ 2:  ", c2)
print("Moeda  R$ 1:  ", m1)
