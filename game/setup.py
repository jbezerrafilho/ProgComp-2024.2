import pygame
from pieces import load_pieces, initial_board

# Constantes
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS
DARK_COLOR = (100, 75, 58)
LIGHT_COLOR = (154, 147, 131)
ERROR_SOUND_PATH = "assets/error.mp3"
SUCCESS_SOUND_PATH = "assets/success.mp3"

def setup_screen():
    """Configura a tela do jogo."""
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Xadrez")
    return screen

def setup_sounds():
    """Configura os sons do jogo."""
    pygame.mixer.init()
    error_sound = pygame.mixer.Sound(ERROR_SOUND_PATH)
    success_sound = pygame.mixer.Sound(SUCCESS_SOUND_PATH)
    return error_sound, success_sound

def setup_game():
    """Inicializa e configura o jogo."""
    pygame.init()

    screen = setup_screen()
    pieces = load_pieces(SQUARE_SIZE)
    board = initial_board()
    error_sound, success_sound = setup_sounds()

    return screen, pieces, board, SQUARE_SIZE, ROWS, COLS, LIGHT_COLOR, DARK_COLOR, error_sound, success_sound
