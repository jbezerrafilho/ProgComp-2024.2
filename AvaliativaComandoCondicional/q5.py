# Developed by J.Bezerra e Eduarda
# Novembro de 2024
try:
    print()
    print('Calendário Juliano.')
    dia = int(input('Informe o dia: '))
    mes = int(input('Informe o mês: '))
    ano = int(input('Informe o ano: '))
    dia_juliano = dia
    data_valida = False
    bissexto = False
    ano_valido = True

    # Validando se o ano é válido e bissexto
    if ano < 0:
        ano_valido = False
        print('Ano inválido!\n')
    elif (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        bissexto = True


    if ano_valido:
        # Validando dia do mês
        if  mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            if dia >= 1 and dia <= 31:
                data_valida = True
            else:
                print('Dia inválido')
        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
            if dia >= 1 and dia <= 30:
                data_valida = True   
            else:
                print('Dia inválido')
        elif mes == 2 and bissexto:
            if dia >= 1 and dia <= 29:
                data_valida = True
        elif mes == 2: 
            if dia >= 1 and dia <= 28:
                data_valida = True
            else:
                print('Dia inválido')
        else: 
            print('Data inválida')
        

    # Calculando o dia Juliano
    if data_valida:
        if mes > 1:
            dia_juliano += 31 # Janeiro
        if mes > 2 :
            dia_juliano += 29 if bissexto else 28 # Fevereiro
        if mes > 3:
            dia_juliano += 31 # Março
        if mes > 4:
            dia_juliano += 30 # Abril
        if mes > 5:
            dia_juliano += 31 # Maio
        if mes > 6:
            dia_juliano += 30 # Junho
        if mes > 7:
            dia_juliano += 31 # Julho
        if mes > 8: 
            dia_juliano += 31 # Agosto
        if mes > 9:
            dia_juliano += 30 # Setembro
        if mes > 10:
            dia_juliano += 31 # Outubro
        if mes > 11:
            dia_juliano += 30 # Novembro

    print(f'Seu dia juliano é {dia_juliano}.') if data_valida else None

except ValueError as e:
    print(e)
    print('Digite um número válido!')