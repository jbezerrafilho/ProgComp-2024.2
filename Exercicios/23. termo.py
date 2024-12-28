import random
palavras = (
    "ADAGA", "ADUBO", "AMIGO", "ANEXO", "ARAME", "ARARA", "ARROZ",
    "ASILO", "ASTRO", "BAILE", "BAIXA", "BALAO", "BALSA", "BARCO",
    "BARRO", "BEIJO", "BICHO", "BORDA", "BORRA", "BRAVO", "BREJO",
    "BURRO", "CAIXA", "CALDO", "CANJA", "CARRO", "CARTA", "CERVO",
    "CESTA", "CLIMA", "COBRA", "COLAR", "COQUE", "COURO", "CRAVO",
    "DARDO", "FAIXA", "FARDO", "FENDA", "FERRO", "FESTA", "FLUOR",
    "FORCA", "FORNO", "FORTE", "FUNDO", "GAITA", "GARRA", "GENIO",
    "GESSO", "GRADE", "GRANA", "GRAMA", "GURIA", "GREVE", "GRUTA",
    "HEROI", "HOTEL", "ICONE", "IMPAR", "IMUNE", "INDIO", "JUNTA",
    "LAPIS", "LARVA", "LAZER", "LENTO", "LESTE", "LIMPO", "LIVRO",
    "MACIO", "MAGRO", "MALHA", "MANSO", "MARCO", "METAL", "MORTE",
    "MORRO", "MURAL", "MOVEL", "NACAO", "NINHO", "NOBRE", "NORMA",
    "NORTE", "NUVEM", "PACTO", "PALHA", "PARDO", "PARTE", "PEDRA",
    "PEDAL", "PEIXE", "PRADO", "PISTA", "POMBO", "POETA", "PONTO",
    "PRATO", "PRECO", "PRESO", "PROSA", "PRUMO", "PULGA", "PULSO",
    "QUEPE", "RAIVA", "RISCO", "RITMO", "ROSTO", "ROUPA", "SABAO",
    "SALTO", "SENSO", "SINAL", "SITIO", "SONHO", "SOPRO", "SURDO",
    "TARDE", "TERNO", "TERMO", "TERRA", "TIGRE", "TINTA", "TOLDO",
    "TORRE", "TRAJE", "TREVO", "TROCO", "TRONO", "TURMA", "URUBU",
    "VALSA", "VENTO", "VERDE", "VISAO", "VINHO", "VIUVO", "ZEBRA"
)

sorteada = random.choice(palavras)
tentativas = 6
atual =  "_" * len(sorteada)
RED = '\033[31;m'
GREEN = '\033[32;m'
YELLOW = '\033[33;m'
DEFAULT = '\033[m'

print('JOGO DO TERMO')
print('Atenção as regras:')
print('** Descubra a palavra certa. Você tem 6 tentativas!!')
print('** Uma letra na cor'+ GREEN + ' Verde '+ DEFAULT + 'significa que a mesma faz parte \
da palavra e está na posição correta.')
print('** Uma letra na cor'+ YELLOW + ' Amarela '+ DEFAULT + 'significa que a mesma faz parte \
da palavra, mas está em outra posição.')
print('** Uma letra na cor'+ RED + ' Vermelha '+ DEFAULT + 'significa que a mesma não faz parte \
da palavra.')
print('** Podem existir letras repetidas!!')
print()
print(atual)



while (atual != sorteada) and (tentativas > 0):
   
    palavra = input('Digite uma palavra: ').upper()
    while len(palavra) != 5:
        palavra = input('Digite uma palavra com 5 letras: ').upper() 
    # String é imutável
    nova = ''
    for pos in range(len(sorteada)):
        if palavra == sorteada:
            nova = sorteada
            break
        elif palavra[pos] == sorteada[pos]:
            nova = nova + GREEN + sorteada[pos] + DEFAULT         
        elif palavra[pos] in sorteada:
            nova = nova + YELLOW + palavra[pos] + DEFAULT
        else:
            nova = nova + RED + palavra[pos] + DEFAULT
        
    atual = nova
    if atual == sorteada and tentativas == 6:
        print(GREEN + atual + DEFAULT)
        print("Genial!!")
    elif atual == sorteada and tentativas == 5:
        print(GREEN + atual + DEFAULT)
        print("Fantástico!!")
    elif atual == sorteada and tentativas == 4:
        print(GREEN + atual + DEFAULT)
        print("Extraordinário!!")
    elif atual == sorteada and tentativas == 3:
        print(GREEN + atual + DEFAULT)
        print("Fenomenal!!")
    elif atual == sorteada and tentativas == 2:
        print(GREEN + atual + DEFAULT)
        print("Impressionante!!")
    elif atual == sorteada and tentativas == 1:
        print(GREEN + atual + DEFAULT)
        print("UFA!!")
    else:
        print(atual)
        
    tentativas -= 1

if atual != sorteada:
    print(f'A palavra sorteada foi {sorteada}!')


