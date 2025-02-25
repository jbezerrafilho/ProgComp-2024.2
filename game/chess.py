import pygame
from pieces import load_pieces, initial_board  # Importando do arquivo pieces.py

# Inicializa o Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# Cores
#WHITE = (232, 235, 239)   # um tom claro (por ex. quase branco)
DARK_COLOR = (79, 42, 43)
#DARK_COLOR  = (125, 135, 150)   # um tom escuro  (por ex. cinza azulado)
LIGHT_COLOR = (121, 76, 64) # Marron

# Tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Xadrez")

# Carregar peças e tabuleiro inicial
pieces = load_pieces(SQUARE_SIZE)
board = initial_board()

def draw_board():
    """Desenha o tabuleiro."""
    for row in range(ROWS):
        for col in range(COLS):
            color = LIGHT_COLOR if (row + col) % 2 == 0 else DARK_COLOR
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def draw_pieces():
    """Desenha as peças no tabuleiro."""
    for row in range(ROWS):
        for col in range(COLS):
            piece = board[row][col]  # Obtém a peça na posição (row, col)
            if piece:  # Se houver uma peça na posição
                # Desenha a imagem da peça no centro do quadrado
                screen.blit(pieces[piece], (col * SQUARE_SIZE, row * SQUARE_SIZE))

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Desenha o tabuleiro e as peças
        draw_board()
        draw_pieces()
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()