conta = int(input('Qual o valor da conta? '))
pago = int(input('Quanto o cliente pagou? '))
troco = pago - conta

# Verifica se o valor pago é suficiente
while troco < 0:
    print('O valor pago é insuficiente!')
    pago = int(input('Quanto o cliente pagou? '))
    troco = pago - conta

# Denominações de moedas
denominacoes = [200, 100, 50, 20, 10, 5, 2, 1]

# Calcula o troco
for valor in denominacoes:
    cedula = troco // valor
    troco = troco % valor
    if cedula != 0:
        print(f'Cédula R$ {valor}: {cedula}')


