palavras = ['LAPIS', 'TEXTO', 'LINHAS', 'CORES']

sorteada = 'LAPIS'
atual = "_" * len(sorteada)
tentativas = 6
GREEN = "\033[0;32m"
BLUE  = "\033[1;34m"
RED   = "\033[1;31m"  

while (atual != sorteada) and (tentativas > 0):
    palavra = input('Digite uma palavra: ').upper()
    # A variável 'nova' foi criada porque não podemos atualizar atual 
    # Lmebre-se que String é invariável

    nova = ''
    if palavra == sorteada:
        nova = sorteada
    else:
        for posicao in range(len(sorteada)):
            if sorteada[posicao] == palavra[posicao]:
                nova = nova + sorteada[posicao]             
            elif palavra[posicao] in sorteada:
                nova = nova + palavra[posicao]
            else:
                nova = nova + atual[posicao]
    print(nova)
    atual = nova
    tentativas -= 1

if atual == sorteada:
    print('Parabéns!!')
else:
    print('Lamento!!')
