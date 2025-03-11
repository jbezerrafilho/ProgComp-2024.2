import pygame
from rules import move_piece

def get_square_under_mouse(SQUARE_SIZE):
    mouse_pos = pygame.mouse.get_pos()
    x, y = mouse_pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def handle_events(game_state):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_state['running'] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            row, col = get_square_under_mouse(game_state['SQUARE_SIZE'])
            piece = game_state['board'][row][col]
            if piece != '' and piece[0] == game_state['current_player']:
                game_state['selected_piece'] = piece
                game_state['selected_pos'] = (row, col)
                game_state['dragging'] = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if game_state['dragging']:
                row, col = get_square_under_mouse(game_state['SQUARE_SIZE'])
                if game_state['selected_piece']:
                    target_pos = row, col
                    if target_pos == game_state['selected_pos']:
                        # Reposiciona a peça na posição original
                        row = game_state['selected_pos'][0]
                        col = game_state['selected_pos'][1]
                        game_state['board'][row][col] = game_state['selected_piece']
                    else:
                        # Tenta mover a peça para a nova posição
                        if move_piece(
                            game_state['board'], 
                            game_state['selected_piece'], 
                            game_state['selected_pos'], 
                            target_pos, 
                            game_state['success_sound'], 
                            game_state['error_sound']
                        ):
                            # Alterna o jogador atual
                            game_state['current_player'] = 'b' if game_state['current_player'] == 'w' else 'w'
                    # Reseta o estado de seleção e arrasto
                    game_state['selected_piece'] = None
                    game_state['selected_pos'] = None
                    game_state['dragging'] = False
    return game_state