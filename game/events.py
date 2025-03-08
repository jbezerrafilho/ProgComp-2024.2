import pygame
from rules import move_piece  


# Retorna a linha e a coluna do quadrado sob o mouse.
def get_square_under_mouse(SQUARE_SIZE):
    mouse_pos = pygame.mouse.get_pos()
    x, y = mouse_pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

# Processa os eventos do jogo, como cliques do mouse e movimentos das peças.
def handle_events(board, selected_piece, selected_pos, dragging, success_sound, error_sound, SQUARE_SIZE):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False, selected_piece, selected_pos, dragging
        elif event.type == pygame.MOUSEBUTTONDOWN:
            row, col = get_square_under_mouse(SQUARE_SIZE)
            if board[row][col] != '':
                selected_piece = board[row][col]
                selected_pos = (row, col)
                dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if dragging:
                row, col = get_square_under_mouse(SQUARE_SIZE)
                if selected_piece:
                    target_pos = (row, col)
                    if target_pos == selected_pos:
                        # Se a peça foi solta na mesma posição, restaura a peça
                        board[selected_pos[0]][selected_pos[1]] = selected_piece
                    else:
                        move_piece(board, selected_piece, selected_pos, target_pos, success_sound, error_sound)
                    selected_piece = None
                    selected_pos = None
                    dragging = False
    return True, selected_piece, selected_pos, dragging