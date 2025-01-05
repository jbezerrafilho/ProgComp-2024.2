# Developed by J.Bezerra 
# Janeiro de 2025

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
# >1969---------------Dias calculados------------------2024<
for ano in range(ano_0 + 1, 2025):
   if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        qtd_dias += 366
   else:
        qtd_dias += 365



# Calculando os dias do ano zero
# >27/04/1968----------Dias calculados-----------31/12/1968<
qtd_dias += 30 - dia_0
for mes in range(mes_0, 13):
    if mes in [5, 7, 8, 10, 12]:
        qtd_dias += 31 
    elif mes in [6, 9, 11]:
        qtd_dias += 30 
#

# Calculando os dias do ano atual   
# >01/01/2025----------Dias calculados-----------data_atual<
for mes in range(1, mes_atual + 1):
    if mes == mes_atual:
        qtd_dias += dia_atual
    elif mes in [1, 5, 7, 8, 10, 12]: 
        qtd_dias += 31 
    elif mes in [4, 6, 9, 11]:
        qtd_dias += 30   

# Calculando a quantidade de sábados
qtd_sabados = 0
dia_da_semana = 0  # 0 = segunda, 1 = terça, ..., 5 = sábado, 6 = domingo
for ano in range(ano_0, ano_atual + 1):
    for mes in range(1, 13):
        if mes in [1, 3, 5, 7, 8, 10, 12]:
            dias_no_mes = 31
        elif mes in [4, 6, 9, 11]:
            dias_no_mes = 30
        elif mes == 2:
            if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
                dias_no_mes = 29
            else:
                dias_no_mes = 28

        for dia in range(1, dias_no_mes + 1):
            if ano == ano_0 and mes == mes_0 and dia < dia_0:
                continue
            if ano == ano_atual and mes == mes_atual and dia > dia_atual:
                break
            if dia_da_semana == 5:  # 5 representa sábado
                qtd_sabados += 1
            dia_da_semana = (dia_da_semana + 1) % 7  # Atualiza o dia da semana



print(f"Quantidade de dias entre {dia_0}/{mes_0}/{ano_0} e {dia_atual}/{mes_atual}/{ano_atual}: {qtd_dias} dias")
print(f'A quantidade de sábados no intervalo acima é: {qtd_sabados}')