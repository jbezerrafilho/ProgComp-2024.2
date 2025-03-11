import pygame

def load_pieces(square_size):
    pieces = {
        'wp': pygame.transform.scale(pygame.image.load('assets/w_pawn.png'), (square_size, square_size)),
        'wr': pygame.transform.scale(pygame.image.load('assets/w_rook.png'), (square_size, square_size)),
        'wn': pygame.transform.scale(pygame.image.load('assets/w_knight.png'), (square_size, square_size)),
        'wb': pygame.transform.scale(pygame.image.load('assets/w_bishop.png'), (square_size, square_size)),
        'wq': pygame.transform.scale(pygame.image.load('assets/w_queen.png'), (square_size, square_size)),
        'wk': pygame.transform.scale(pygame.image.load('assets/w_king.png'), (square_size, square_size)),
        'bp': pygame.transform.scale(pygame.image.load('assets/b_pawn.png'), (square_size, square_size)),
        'br': pygame.transform.scale(pygame.image.load('assets/b_rook.png'), (square_size, square_size)),
        'bn': pygame.transform.scale(pygame.image.load('assets/b_knight.png'), (square_size, square_size)),
        'bb': pygame.transform.scale(pygame.image.load('assets/b_bishop.png'), (square_size, square_size)),
        'bq': pygame.transform.scale(pygame.image.load('assets/b_queen.png'), (square_size, square_size)),
        'bk': pygame.transform.scale(pygame.image.load('assets/b_king.png'), (square_size, square_size)),
    }
    return pieces

def initial_board():
    board = [
        ['br', 'bn', 'bb', 'bq', 'bk', 'bb', 'bn', 'br'],
        ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
        ['wr', 'wn', 'wb', 'wq', 'wk', 'wb', 'wn', 'wr'],
    ]
    return board





