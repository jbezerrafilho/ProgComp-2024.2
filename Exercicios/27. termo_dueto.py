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
    "MACIO", "MAGRO", "MALHA", "MANSO", "MARCO", "METAL", "MORAL",
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

#sorteada_1 = random.choice(palavras)
sorteada_1 = 'SUSHI'
#sorteada_2 = random.choice(palavras)
sorteada_2 = 'TECLA'
tentativas = 6
RED = '\033[1;31;m'
GREEN = '\033[1;32;m'
YELLOW = '\033[1;33;m'
DEFAULT = '\033[m'

print(f"""
JOGO DO TERMO - DUETO
Atenção às regras:
** Descubra a palavra certa. Você tem 6 tentativas!!
** Uma letra na cor {GREEN}Verde{DEFAULT} está na {GREEN}posição correta{DEFAULT} da palavra.
** Uma letra na cor {YELLOW}Amarela{DEFAULT} está {YELLOW}posiçao incorreta{DEFAULT} da palavra.
** Uma letra na cor {RED}Vermelho{DEFAULT} não faz parte da palavra.
** Podem existir letras repetidas!!
""")

termo1 = ''
termo2 = ''
acerto_termo1 = False
acerto_termo2 = False
while tentativas > 0 and (not acerto_termo1 or not acerto_termo2):
    
    palavra = input('Digite uma palavra: ').upper()
    # Tratando a entrada do usuário
    while len(palavra) != 5:
        palavra = input('Digite uma palavra com 5 letras: ').upper() 
   
    termo1 = termo1 + '\n'
    pos = 0
    while pos < len(sorteada_1) and not acerto_termo1:
        if palavra == sorteada_1:
            termo1 = termo1 + GREEN + sorteada_1 + DEFAULT
            acerto_termo1 = True
            break
        elif palavra[pos] == sorteada_1[pos]:
            termo1 = termo1 + GREEN + sorteada_1[pos] + DEFAULT         
        elif palavra[pos] in sorteada_1:
            termo1 = termo1 + YELLOW + palavra[pos] + DEFAULT
        else:
            termo1 = termo1 + RED + palavra[pos] + DEFAULT 
        pos += 1
        
    print(termo1)
    

    termo2 = termo2 + '\n'
    pos1 = 0
    while pos1 < len(sorteada_2) and not acerto_termo2:
        if palavra == sorteada_2:
            termo2 = termo2 + GREEN + sorteada_2 + DEFAULT
            acerto_termo2 = True
            break
        elif palavra[pos1] == sorteada_2[pos1]:
            termo2 = termo2 + GREEN + sorteada_1[pos1] + DEFAULT         
        elif palavra[pos1] in sorteada_2:
            termo2 = termo2 + YELLOW + palavra[pos1] + DEFAULT
        else:
            termo2 = termo2 + RED + palavra[pos1] + DEFAULT 
        pos1 += 1

    print(termo2)


    tentativas -= 1






