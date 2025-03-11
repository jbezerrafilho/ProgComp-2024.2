import pygame
from pieces import load_pieces, initial_board

# Constantes
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS
DARK_COLOR = (0, 0, 0)
LIGHT_COLOR = (246, 201, 137)
ERROR_SOUND_PATH = "assets/error.mp3"
SUCCESS_SOUND_PATH = "assets/success.mp3"

# Inicializa e configura o jogo
def setup_game():
    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Xadrez")

    pieces = load_pieces(SQUARE_SIZE)
    board = initial_board()
    error_sound = pygame.mixer.Sound(ERROR_SOUND_PATH)
    success_sound = pygame.mixer.Sound(SUCCESS_SOUND_PATH)

    return {
        'screen': screen,
        'pieces': pieces,
        'board': board,
        'SQUARE_SIZE': SQUARE_SIZE,
        'ROWS': ROWS,
        'COLS': COLS,
        'LIGHT_COLOR': LIGHT_COLOR,
        'DARK_COLOR': DARK_COLOR,
        'error_sound': error_sound,
        'success_sound': success_sound,
        'selected_piece': None,
        'selected_pos': None,
        'dragging': False,
        'running': True,
        'current_player': 'w'
    }
