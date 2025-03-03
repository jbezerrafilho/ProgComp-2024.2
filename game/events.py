import pygame
from rules import (
    is_pawn_move_valid, is_rook_move_valid, is_knight_move_valid,
    is_bishop_move_valid, is_queen_move_valid, is_king_move_valid,
    move_piece  
)

def get_square_under_mouse(SQUARE_SIZE):
    """
    Obtém a posição do quadrado sob o cursor do mouse.
    """
    mouse_pos = pygame.mouse.get_pos()
    x, y = mouse_pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def handle_events(board, selected_piece, selected_pos, dragging, success_sound, error_sound, SQUARE_SIZE):
    """
    Processa os eventos do jogo, como cliques do mouse e movimentos das peças.
    """
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
                    if (row, col) == selected_pos:
                        # Se a peça foi solta na mesma posição, restaura a peça
                        board[selected_pos[0]][selected_pos[1]] = selected_piece
                    else:
                        move_piece(board, selected_piece, selected_pos, (row, col), success_sound, error_sound)
                    selected_piece = None
                    selected_pos = None
                    dragging = False
    return True, selected_piece, selected_pos, dragging