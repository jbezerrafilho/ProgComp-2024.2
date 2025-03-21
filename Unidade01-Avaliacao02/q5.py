# Developed by J.Bezerra 
# Janeiro de 2025

import datetime

# Data atual
date = datetime.datetime.today()
dia_atual = date.day
mes_atual = date.month
ano_atual = date.year

# Data Inicial
dia_inicial, mes_inicial, ano_inicial = 27, 4, 1968 # Por ser dia 0, não será incluso na contagem
qtd_dias = 0

# Calculando os dias completos dos anos intermediários
# >1969---------------Dias calculados------------------2024<
for ano in range(ano_inicial + 1, 2025):
   if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        qtd_dias += 366
   else:
        qtd_dias += 365

# Calculando os dias do ano inicial
# >27/04/1968----------Dias calculados-----------31/12/1968<
for mes in range(mes_inicial, 13):
    if mes == mes_inicial and mes in [1, 3, 5, 7, 8, 10, 12]:
        qtd_dias += 31 - dia_inicial 
    elif mes == mes_inicial and mes in [4, 6, 9, 11]:
        qtd_dias += 30 - dia_inicial 
    elif mes == mes_inicial and mes == 2:
        if (ano_inicial % 4 == 0 and ano_inicial % 100 != 0) or (ano_inicial % 400 == 0):
            qtd_dias += 29 - dia_inicial 
        else:
            qtd_dias += 28 - dia_inicial 
    elif mes in [1, 3, 5, 7, 8, 10, 12]:
        qtd_dias += 31 
    elif mes in [4, 6, 9, 11]:
        qtd_dias += 30 
    elif mes == 2:
        if (ano_inicial % 4 == 0 and ano_inicial % 100 != 0) or (ano_inicial % 400 == 0):
            qtd_dias += 29
        else:
            qtd_dias += 28


# Calculando os dias do ano atual   
# >01/01/2025----------Dias calculados-----------data_atual<
for mes in range(1, mes_atual + 1):
    if mes == mes_atual:
        qtd_dias += dia_atual
    elif mes in [1, 5, 7, 8, 10, 12]: 
        qtd_dias += 31 
    elif mes in [4, 6, 9, 11]:
        qtd_dias += 30 
    elif mes == 2:
        qtd_dias += 28 if (ano_atual % 4 != 0) or \
            (ano_atual % 100 == 0 and ano_atual % 400 != 0) else 29

qtd_sabados = 0

# A divisão inteira de (qtd_dias + 6) por 7 é a quantidade de sábados
# O '+6' é para arredondar para cima, pois a divisão inteira arredonda para baixo
# Podemos fazer isso porque o dia 0 é um sábado
qtd_sabados = (qtd_dias + 6) // 7


print(f"Quantidade de dias entre {dia_inicial}/{mes_inicial}/{ano_inicial} e {dia_atual}/{mes_atual}/{ano_atual}: {qtd_dias} dias")
print(f'A quantidade de sábados no intervalo acima é: {qtd_sabados}')