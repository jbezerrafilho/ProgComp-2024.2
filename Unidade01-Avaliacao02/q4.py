# Developed by J.Bezerra 
# Janeiro de 2025

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
RED = '\033[1;31m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
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
** Selecione PALAVRAS do conjunto ABAIXO!
"""

print(msg)

# O próximo trecho de código até o 'print' na linha 55 formata a impressão da tupla 'palavras'
palavras_linha = 7
contador = 0
for palpite in palavras:
    print(palpite, end='  ')
    contador += 1
    if contador == palavras_linha:
        print()
        contador = 0
print()

# Variável criada para acumular os palpites digitados
termos = '1ºTermo  2ºTermo \n'

# Variáveis para validar o acerto do usuário
acertou_termo1 = False
acertou_termo2 = False

# Variável criada para formatar a saída do texto
alinhar = 9 * ' '
    

# Laço principal. Será controlado em função das tentativas e acertos
while tentativas > 0 and (not acertou_termo1 or not acertou_termo2):
    
    palpite = input('Digite uma palavra: ').strip().upper()

    # Tratando a entrada do usuário
    while palpite not in palavras:
        palpite = input('Digite uma palavras do conjunto acima ⬆️: ').strip().upper() 

    # Armazenam o 'palpite' atual do laço e adiciona as cores 
    atual_1 = '' 
    atual_2 = '' 

    # Lógica para comparar o palpite com o termo 1 (sorteada_1)
    # Iteramos sobre cada letra da palavra digitada e definimos a cor
    pos = 0 
    while pos < len(sorteada_1) and not acertou_termo1:
        if palpite == sorteada_1:
            atual_1 += GREEN + sorteada_1 + DEFAULT
            acertou_termo1 = True 
            break
        elif palpite[pos] == sorteada_1[pos]:
            atual_1 += GREEN + sorteada_1[pos] + DEFAULT         
        elif palpite[pos] in sorteada_1:
            atual_1 += YELLOW + palpite[pos] + DEFAULT
        else:
            atual_1 += RED + palpite[pos] + DEFAULT 
        pos += 1
   
    # Agora, comparamos o palpite com o termo 2 (sorteada_2)
    pos = 0 
    while pos < len(sorteada_2) and not acertou_termo2:
        if palpite == sorteada_2:
            atual_2 += GREEN + sorteada_2 + DEFAULT
            acertou_termo2 = True # Controle do laço
            break
        elif palpite[pos] == sorteada_2[pos]:
            atual_2 += GREEN + sorteada_2[pos] + DEFAULT          
        elif palpite[pos] in sorteada_2:
            atual_2 += YELLOW + palpite[pos] + DEFAULT    
        else:
            atual_2 += RED + palpite[pos] + DEFAULT 
        pos += 1
    
    # Exibindo os 'palpites com as cores' acumulados durante as tentativas
    if atual_1 == '':
        termos += alinhar + atual_2 + '\n' 
        print(termos)
    elif atual_2 == '':
        termos += atual_1 + alinhar + '\n'
        print(termos)
    else:
        termos += atual_1 + '    ' + atual_2 + '\n'
        print(termos)
    
    tentativas -= 1

# Finalizando o jogo após as tentativas!
if acertou_termo1 and acertou_termo2:
    print('Genial!!')
if not acertou_termo1:
    print(f'O primeiro termo é {sorteada_1}!')
if not acertou_termo2:
    print(f'O segundo termo é {sorteada_2}!')



