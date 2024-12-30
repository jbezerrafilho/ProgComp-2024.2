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

# Definindo cores no Python
RED = '\033[1;31;m'
GREEN = '\033[1;32;m'
YELLOW = '\033[1;33;m'
DEFAULT = '\033[m'

# Definindo variáveis importantes - auto explicativas
sorteada_1 = random.choice(palavras)
sorteada_2 = random.choice(palavras)
tentativas = 7
msg = f"""
JOGO DO TERMO - DUETO
** Descubra a palavra certa. Você tem {tentativas} tentativas!!
** Uma letra na cor {GREEN}Verde{DEFAULT} está na {GREEN}posição correta{DEFAULT} da palavra.
** Uma letra na cor {YELLOW}Amarela{DEFAULT} está {YELLOW}posiçao incorreta{DEFAULT} da palavra.
** Uma letra na cor {RED}Vermelho{DEFAULT} não faz parte da palavra.
** Somente PALAVRAS do conjunto abaixo serão aceitas com ENTRADA!
"""

print(msg)

# O próximo trecho de código até o 'print' na linha 55 formata a impressão da tupla 'palavras'
palavras_linha = 7
contador = 0
for palavra in palavras:
    print(palavra, end='  ')
    contador += 1
    if contador == palavras_linha:
        print()
        contador = 0
print()

# Cada palavra digitada será acumulada em ambas variáveis
termo1 = ''
termo2 = ''

# Variáveis de controle dos laços internos 
acerto_termo1 = False
acerto_termo2 = False

while tentativas > 0 and (not acerto_termo1 or not acerto_termo2):
    
    palavra = input('Digite uma palavra: ').upper()

    # Tratando a entrada do usuário
    while palavra not in palavras:
        palavra = input('Digite uma palavra válida com 5 letras: ').upper() 
   

    pos = 0 # 1ª variável de controle do laço
    termo1 += '\n' 
    # Iteramos sobre cada letra da palavra digitada
    while pos < len(sorteada_1) and not acerto_termo1:
        if palavra == sorteada_1:
            termo1 += GREEN + sorteada_1 + DEFAULT
            acerto_termo1 = True # 2ª Variável de controle alterada
            break
        elif palavra[pos] == sorteada_1[pos]:
            termo1 += GREEN + sorteada_1[pos] + DEFAULT         
        elif palavra[pos] in sorteada_1:
            termo1 += YELLOW + palavra[pos] + DEFAULT
        else:
            termo1 += RED + palavra[pos] + DEFAULT 
        pos += 1
    print(termo1) 
    
    
    pos = 0 # 1ª variável de controle do laço
    termo2 += '\n'

    # Iteramos sobre cada letra da palavra digitada
    while pos < len(sorteada_2) and not acerto_termo2:
        if palavra == sorteada_2:
            termo2 += GREEN + sorteada_2 + DEFAULT
            acerto_termo2 = True # 2ª Variável de controle
            break
        elif palavra[pos] == sorteada_2[pos]:
            termo2 += GREEN + sorteada_2[pos] + DEFAULT          
        elif palavra[pos] in sorteada_2:
            termo2 += YELLOW + palavra[pos] + DEFAULT    
        else:
            termo2 += RED + palavra[pos] + DEFAULT 
        pos += 1
    print(termo2) 
   
    tentativas -= 1

# Se o jogador errar suas tentativas, informe as palavras sorteadas
if not acerto_termo1:
    print(f'O primeiro termo é {sorteada_1}')
if not acerto_termo2:
    print(f'O segundo termo é {sorteada_2}')



