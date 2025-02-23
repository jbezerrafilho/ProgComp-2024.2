import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configurações do tabuleiro
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# Cores
WHITE = (240, 217, 181)
BLACK = (181, 136, 99)

# Carregar imagens das peças
PIECES = {
    "b_pawn": pygame.image.load("pieces/b_pawn.png"),
    "w_pawn": pygame.image.load("pieces/w_pawn.png"),
    "b_rook": pygame.image.load("pieces/b_rook.png"),
    "w_rook": pygame.image.load("pieces/w_rook.png"),
    # Adicione as outras peças...
}

# Ajustar tamanho das imagens
for key in PIECES:
    PIECES[key] = pygame.transform.scale(PIECES[key], (SQUARE_SIZE, SQUARE_SIZE))

# Inicializar tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess in Pygame")

def draw_board():
    """Desenha o tabuleiro de xadrez"""
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def draw_pieces(board):
    """Desenha as peças no tabuleiro"""
    for row in range(ROWS):
        for col in range(COLS):
            piece = board[row][col]
            if piece:
                screen.blit(PIECES[piece], (col * SQUARE_SIZE, row * SQUARE_SIZE))

# Estado inicial do tabuleiro
initial_board = [
    ["b_rook", None, None, None, None, None, None, "b_rook"],
    ["b_pawn"] * 8,
    [None] * 8,
    [None] * 8,
    [None] * 8,
    [None] * 8,
    ["w_pawn"] * 8,
    ["w_rook", None, None, None, None, None, None, "w_rook"],
]

def main():
    """Loop principal do jogo"""
    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_board()
        draw_pieces(initial_board)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
