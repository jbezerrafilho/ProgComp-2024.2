# Developed by J.Bezerra e Eduarda
# Novembro de 2024

try:
    ano = int(input('Informe o ano para saber se é bissexto: '))

    # Validando se o ano é bissexto
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f'{ano} é Bissexto!')
    else:
        print(f'{ano} NÃO é Bissexto!')


except ValueError as e:
    print(e)
    print('Informe um ano válido!')