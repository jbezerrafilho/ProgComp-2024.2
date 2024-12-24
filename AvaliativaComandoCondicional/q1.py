# Developed by J.Bezerra e Eduarda
# Novembro de 2024

try:
    print('Calculadora de IMC')
    peso = float(input('Informe seu peso em Kg: '))
    altura = float(input('Informe sua altura em m: '))
    imc = round(peso / (altura ** 2), 1)
    print('Seu IMC é:', imc)
    situacao = ''

    if imc <= 18.5:
        situacao = 'Abaixo do peso'
    elif 18.6 <= imc <= 24.9:
        situacao = 'Peso normal'
    elif 25.0 <= imc <= 29.9:
        situacao = 'Sobrepeso'
    elif 30 <= imc <= 34.9:
        situacao = 'Obesidade grau 1'
    elif 35 <= imc <= 39.9:
        situacao = 'Obesidade grau 2'
    else:
       situacao = 'Obesidade grau 3'
    
    print(situacao)
    
except ValueError as e:
    print(e)
    print('Digite um número válido!')