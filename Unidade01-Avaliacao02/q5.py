import datetime

# Data atual
date = datetime.datetime.today()
dia_atual = date.day
mes_atual = date.month
ano_atual = date.year

# Data Zero
dia_0 = 27
mes_0 = 4
ano_0 = 1968

qtd_dias = 0

# Calculando os dias completos dos anos intermediários
for ano in range(ano_0 + 1, 2025):
   if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        qtd_dias += 366
   else:
        qtd_dias += 365
   

# Calculando os dias do ano zero
qtd_dias += 30 - dia_0
for mes in range(mes_0, 13):
    if mes in [5, 7, 8, 10, 12]:
        qtd_dias += 31 
    elif mes in [6, 9, 11]:
        qtd_dias += 30 


# Calculando os dias do ano atual   
for mes in range(1, mes_atual + 1):
    if mes == mes_atual:
        qtd_dias += dia_atual
    elif mes in [1, 5, 7, 8, 10, 12]: 
        qtd_dias += 31 
    elif mes in [4, 6, 9, 11]:
        qtd_dias += 30           
print(qtd_dias)


print(f"Quantidade de dias entre {dia_0}/{mes_0}/{ano_0} e {dia_atual}/{mes_atual}/{ano_atual}: {qtd_dias} dias")