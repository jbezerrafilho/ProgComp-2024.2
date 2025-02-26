import pygame
from pieces import load_pieces, initial_board  # Importando do arquivo pieces.py
from draw import draw_board, draw_pieces  # Importando do arquivo draw.py

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

selected_piece = None
selected_pos = None
dragging = False

def get_square_under_mouse():
    mouse_pos = pygame.mouse.get_pos()
    x, y = mouse_pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    global selected_piece, selected_pos, dragging
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                row, col = get_square_under_mouse()
                if board[row][col] != '':
                    selected_piece = board[row][col]
                    selected_pos = (row, col)
                    dragging = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if dragging:
                    row, col = get_square_under_mouse()
                    if selected_piece:
                        # Move a peça para a nova posição
                        board[row][col] = selected_piece
                        board[selected_pos[0]][selected_pos[1]] = ''
                        selected_piece = None
                        selected_pos = None
                        dragging = False
            elif event.type == pygame.MOUSEMOTION:
                if dragging:
                    mouse_pos = pygame.mouse.get_pos()
                    x, y = mouse_pos

        # Desenha o tabuleiro e as peças
        draw_board(screen, ROWS, COLS, SQUARE_SIZE, LIGHT_COLOR, DARK_COLOR)
        draw_pieces(screen, board, pieces, SQUARE_SIZE)
        if dragging and selected_piece:
            # Desenha a peça sendo arrastada
            mouse_pos = pygame.mouse.get_pos()
            x, y = mouse_pos
            # Desenha a peça sendo arrastada na posição do mouse
            screen.blit(pieces[selected_piece], (x - SQUARE_SIZE // 2, y - SQUARE_SIZE // 2))
            # Remove a peça original do tabuleiro temporariamente
            board[selected_pos[0]][selected_pos[1]] = ''
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()