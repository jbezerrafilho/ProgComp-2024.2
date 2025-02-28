try:
    num = int(input('Digite um número: '))
    resultado = 10 / num
except ValueError:
    print('Erro: Digite um número válido!')
except ZeroDivisionError:
    print('Divisão por zero NÃO pode!')
else:
    print(f'O resultado da divião é {resultado}')
finally:
    print('Fim da execução')