# Developed by J.Bezerra e Eduarda
# Novembro de 2024

try:
    print()
    print('Desempenho Acadêmico no IFRN')
    print('Cálculo de média em Disciplinas!\n')

    msg = 'Digite a nota entre 0 e 100: '
    situacao = ''
    n1 = float(input(msg))
    n2 = float(input(msg))
    prova_final = False
    
    # Média da Disciplina
    md = (2 * n1 + 3 * n2) / 5
    print('A média da disciplina foi: ', md)
    if md >= 60:
        situacao = 'Aprovado'
        print(situacao)
    elif 20 <= md < 60:
        situacao = 'Em prova final'
        print(situacao)
        prova_final = True    
    else:
        situacao = 'Reprovado'
        print(situacao)
    
    #Três formas de calcular a média final
    if prova_final:
        naf = float(input(msg)) #nota de avaliação final
        mfd = (md + naf) / 2 #1
        mfd1 = (2 * naf + 3 * n2) / 5 #2
        mfd2 = (2 * n1 + 3 * naf) / 5 #3
        if mfd >= 60 or mfd1 >= 60 or mfd2 >= 60:
            situacao = 'Aprovado'
            print(situacao)
        else:
            situacao = 'Reprovado'
            print(situacao)

except ValueError as e:
    print(e)
    print('Digite uma nota válida!')