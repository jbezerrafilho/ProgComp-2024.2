import pygame

# Carregar imagens das peças
def load_pieces(square_size):
    pieces = {
        'wp': pygame.transform.scale(pygame.image.load('assets/w_pawn.png'), (square_size, square_size)),    # Peão branco
        'wr': pygame.transform.scale(pygame.image.load('assets/w_rook.png'), (square_size, square_size)),    # Torre branca
        'wn': pygame.transform.scale(pygame.image.load('assets/w_knight.png'), (square_size, square_size)),  # Cavalo branco
        'wb': pygame.transform.scale(pygame.image.load('assets/w_bishop.png'), (square_size, square_size)),  # Bispo branco
        'wq': pygame.transform.scale(pygame.image.load('assets/w_queen.png'), (square_size, square_size)),   # Rainha branca
        'wk': pygame.transform.scale(pygame.image.load('assets/w_king.png'), (square_size, square_size)),    # Rei branco
        'bp': pygame.transform.scale(pygame.image.load('assets/b_pawn.png'), (square_size, square_size)),    # Peão preto
        'br': pygame.transform.scale(pygame.image.load('assets/b_rook.png'), (square_size, square_size)),    # Torre preta
        'bn': pygame.transform.scale(pygame.image.load('assets/b_knight.png'), (square_size, square_size)),  # Cavalo preto
        'bb': pygame.transform.scale(pygame.image.load('assets/b_bishop.png'), (square_size, square_size)),  # Bispo preto
        'bq': pygame.transform.scale(pygame.image.load('assets/b_queen.png'), (square_size, square_size)),   # Rainha preta
        'bk': pygame.transform.scale(pygame.image.load('assets/b_king.png'), (square_size, square_size)),    # Rei preto
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