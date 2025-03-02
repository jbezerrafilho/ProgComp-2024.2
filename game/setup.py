import pygame
from pieces import load_pieces, initial_board

def setup_game():
    pygame.init()

    WIDTH, HEIGHT = 800, 800
    ROWS, COLS = 8, 8
    SQUARE_SIZE = WIDTH // COLS

    DARK_COLOR = (79, 42, 43)
    LIGHT_COLOR = (121, 76, 64)  # Marron

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Xadrez")

    pieces = load_pieces(SQUARE_SIZE)
    board = initial_board()

    pygame.mixer.init()
    error_sound = pygame.mixer.Sound("assets/error.mp3")
    success_sound = pygame.mixer.Sound("assets/success.mp3")

    return screen, pieces, board, SQUARE_SIZE, ROWS, COLS, LIGHT_COLOR, DARK_COLOR, error_sound, success_sound
