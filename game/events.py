# events.py
import pygame
from rules import (
    is_pawn_move_valid, is_rook_move_valid, is_knight_move_valid,
    is_bishop_move_valid, is_queen_move_valid, is_king_move_valid  # Importa as funções de validação de movimento
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
                        if selected_piece[1] == 'p':  # Verifica se a peça é um peão
                            if is_pawn_move_valid(board, selected_piece, selected_pos, (row, col)):
                                target_piece = board[row][col]
                                if target_piece != '' and selected_piece[0] != target_piece[0]:
                                    success_sound.play()
                                board[row][col] = selected_piece
                                board[selected_pos[0]][selected_pos[1]] = ''
                            else:
                                error_sound.play()
                                board[selected_pos[0]][selected_pos[1]] = selected_piece
                        elif selected_piece[1] == 'r':  # Verifica se a peça é uma torre
                            if is_rook_move_valid(board, selected_piece, selected_pos, (row, col)):
                                target_piece = board[row][col]
                                if target_piece != '' and selected_piece[0] != target_piece[0]:
                                    success_sound.play()
                                board[row][col] = selected_piece
                                board[selected_pos[0]][selected_pos[1]] = ''
                            else:
                                error_sound.play()
                                board[selected_pos[0]][selected_pos[1]] = selected_piece
                        elif selected_piece[1] == 'n':  # Verifica se a peça é um cavalo
                            if is_knight_move_valid(board, selected_piece, selected_pos, (row, col)):
                                target_piece = board[row][col]
                                if target_piece != '' and selected_piece[0] != target_piece[0]:
                                    success_sound.play()
                                board[row][col] = selected_piece
                                board[selected_pos[0]][selected_pos[1]] = ''
                            else:
                                error_sound.play()
                                board[selected_pos[0]][selected_pos[1]] = selected_piece
                        elif selected_piece[1] == 'b':  # Verifica se a peça é um bispo
                            if is_bishop_move_valid(board, selected_piece, selected_pos, (row, col)):
                                target_piece = board[row][col]
                                if target_piece != '' and selected_piece[0] != target_piece[0]:
                                    success_sound.play()
                                board[row][col] = selected_piece
                                board[selected_pos[0]][selected_pos[1]] = ''
                            else:
                                error_sound.play()
                                board[selected_pos[0]][selected_pos[1]] = selected_piece
                        elif selected_piece[1] == 'q':  # Verifica se a peça é uma rainha
                            if is_queen_move_valid(board, selected_piece, selected_pos, (row, col)):
                                target_piece = board[row][col]
                                if target_piece != '' and selected_piece[0] != target_piece[0]:
                                    success_sound.play()
                                board[row][col] = selected_piece
                                board[selected_pos[0]][selected_pos[1]] = ''
                            else:
                                error_sound.play()
                                board[selected_pos[0]][selected_pos[1]] = selected_piece
                        elif selected_piece[1] == 'k':  # Verifica se a peça é um rei
                            if is_king_move_valid(board, selected_piece, selected_pos, (row, col)):
                                target_piece = board[row][col]
                                if target_piece != '' and selected_piece[0] != target_piece[0]:
                                    success_sound.play()
                                board[row][col] = selected_piece
                                board[selected_pos[0]][selected_pos[1]] = ''
                            else:
                                error_sound.play()
                                board[selected_pos[0]][selected_pos[1]] = selected_piece
                        else:
                            # Lógica para outras peças (não alterada)
                            target_piece = board[row][col]
                            if target_piece == '' or selected_piece[0] != target_piece[0]:
                                if target_piece != '' and selected_piece[0] != target_piece[0]:
                                    success_sound.play()
                                board[row][col] = selected_piece
                                board[selected_pos[0]][selected_pos[1]] = ''
                            else:
                                error_sound.play()
                                board[selected_pos[0]][selected_pos[1]] = selected_piece
                    selected_piece = None
                    selected_pos = None
                    dragging = False
    return True, selected_piece, selected_pos, dragging