import pygame

def get_square_under_mouse(SQUARE_SIZE):
    mouse_pos = pygame.mouse.get_pos()
    x, y = mouse_pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def handle_events(board, selected_piece, selected_pos, dragging, success_sound, error_sound, SQUARE_SIZE):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False, selected_piece, selected_pos, dragging
        elif event.type == pygame.MOUSEBUTTONDOWN:
            row, col = get_square_under_mouse(SQUARE_SIZE)  # Obtém a posição do quadrado sob o cursor do mouse
            if board[row][col] != '':                       # Verifique se o quadrado contém peça
                selected_piece = board[row][col]            # Armazene a peça
                selected_pos = (row, col)                   # Armazene a posição da peça
                dragging = True                             # Peça sendo arrastada, isso permite que outras partes do código desenhe a peça sob o cursor sendo arrastada
        elif event.type == pygame.MOUSEBUTTONUP:
            if dragging:
                row, col = get_square_under_mouse(SQUARE_SIZE)
                if selected_piece:
                    if (row, col) == selected_pos:
                        # Se a peça foi solta na mesma posição, restaura a peça
                        board[selected_pos[0]][selected_pos[1]] = selected_piece  
                    else:
                        target_piece = board[row][col]  # Obtém a peça na casa de destino
                        if target_piece == '' or selected_piece[0] != target_piece[0]:  
                            # Move a peça para a nova posição se estiver vazia ou for de cor diferente
                            if target_piece != '' and selected_piece[0] != target_piece[0]:
                                success_sound.play()  # Toca o som de sucesso apenas se houver captura
                            board[row][col] = selected_piece                          
                            board[selected_pos[0]][selected_pos[1]] = ''
                        else:
                            # Se a peça for da mesma cor, alerte o usuario e restaura a peça original
                            error_sound.play()
                            board[selected_pos[0]][selected_pos[1]] = selected_piece
                    selected_piece = None
                    selected_pos = None
                    dragging = False
    return True, selected_piece, selected_pos, dragging