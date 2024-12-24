""""
O ICMS pago pelo consumidor em um produto é em torno de 17%. As empresas
recolhem esse valor ao longo da cadeia de produção/vendas. Assim, se uma
empresa vende um produto por v, tendo comprado por c, ela só recolhe o imposto
relativo à diferença. Faça um programa que aceita os valores de venda e compra
de um produto e mostre o ICMS a ser recolhido pela empresa na operação.
"""
valor_compra = float(input('Digite o valor da compra R$: '))
valor_venda = float(input('Digite o valor da venda R$: '))

#ICMS recolhido em cima da diferença
diferenca = valor_venda - valor_compra
icms = round(diferenca * 0.17, 2)

print(f'O ICMS recolhido será de {icms}.')