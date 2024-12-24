import random
palavras = ['CENOURA', 'TOMATE', 'CEBOLA', 'LARANJA']

sorteada = random.choice(palavras)
atual = "_" * len(sorteada)
tentativas = 2 * len(sorteada)

while (atual != sorteada) and (tentativas > 0):
    letra = input('Digite uma letra: ')
    # A variável 'nova' foi criada porque não podemos atualizar atual 
    # Lmebre-se que String é invariável
    nova = ''

    for posicao in range(len(sorteada)):
        if sorteada[posicao] == letra.upper():
            nova = nova + sorteada[posicao]
        else:
            nova = nova + atual[posicao]
    print(nova)
    atual = nova
    tentativas -= 1

if atual == sorteada:
    print('Parabéns!!')
else:
    print('Lamento!!')