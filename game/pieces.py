import pygame
from pieces import load_pieces, initial_board  # Importando do arquivo pieces.py

# Carregar imagens das peças
def load_pieces():
    pieces = {
        'wp': pygame.image.load('assets/w_pawn.png'),    # Peão branco
        'wr': pygame.image.load('assets/w_rook.png'),    # Torre branca
        'wn': pygame.image.load('assets/w_knight.png'),  # Cavalo branco
        'wb': pygame.image.load('assets/w_bishop.png'),  # Bispo branco
        'wq': pygame.image.load('assets/w_queen.png'),   # Rainha branca
        'wk': pygame.image.load('assets/w_king.png'),    # Rei branco
        'bp': pygame.image.load('assets/b_pawn.png'),    # Peão preto
        'br': pygame.image.load('assets/b_rook.png'),    # Torre preta
        'bn': pygame.image.load('assets/b_knight.png'),  # Cavalo preto
        'bb': pygame.image.load('assets/b_bishop.png'),  # Bispo preto
        'bq': pygame.image.load('assets/b_queen.png'),   # Rainha preta
        'bk': pygame.image.load('assets/b_king.png'),    # Rei preto
    }
    return pieces

# Posição inicial das peças no tabuleiro
def initial_board():
    board = [
        ['br', 'bn', 'bb', 'bq', 'bk', 'bb', 'bn', 'br'],  # Linha 0 (peças pretas)
        ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],  # Linha 1 (peões pretos)
        ['', '', '', '', '', '', '', ''],                   # Linha 2
        ['', '', '', '', '', '', '', ''],                   # Linha 3
        ['', '', '', '', '', '', '', ''],                   # Linha 4
        ['', '', '', '', '', '', '', ''],                   # Linha 5
        ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],  # Linha 6 (peões brancos)
        ['wr', 'wn', 'wb', 'wq', 'wk', 'wb', 'wn', 'wr'],  # Linha 7 (peças brancas)
    ]
    return board