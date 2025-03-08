import pygame

"""Desenha o tabuleiro."""
def draw_board(screen, rows, cols, square_size, light_color, dark_color):
    for row in range(rows):
        for col in range(cols):
            # Determina a cor do quadrado
            color = light_color if (row + col) % 2 == 0 else dark_color
            # Calcula a posição e o tamanho do quadrado
            rect = pygame.Rect(col * square_size, row * square_size, square_size, square_size)
            # Desenha o quadrado no tabuleiro
            pygame.draw.rect(screen, color, rect)

"""Desenha as peças no tabuleiro."""
def draw_pieces(screen, board, pieces, square_size):   
    for row in range(len(board)):
        for col in range(len(board[row])):
            piece = board[row][col]  # Obtém a peça na posição (row, col)
            if piece:  # Se houver uma peça na posição
                # Calcula a posição da peça no centro do quadrado
                piece_x = col * square_size
                piece_y = row * square_size
                # Desenha a imagem da peça no tabuleiro
                screen.blit(pieces[piece], (piece_x, piece_y))

"""Renderiza o tabuleiro e as peças."""
def render(screen, board, pieces, SQUARE_SIZE, ROWS, COLS, LIGHT_COLOR, DARK_COLOR, selected_piece, selected_pos, dragging):
     
    # Desenha o tabuleiro
    draw_board(screen, ROWS, COLS, SQUARE_SIZE, LIGHT_COLOR, DARK_COLOR)
    
    # Desenha as peças no tabuleiro
    draw_pieces(screen, board, pieces, SQUARE_SIZE)
    
    # Se uma peça está sendo arrastada, desenha a peça na posição do mouse
    if dragging and selected_piece:
        mouse_pos = pygame.mouse.get_pos()
        x, y = mouse_pos
        print(x, y)
        # Calcula a posição da peça arrastada para centralizá-la no cursor do mouse
        piece_x = x - SQUARE_SIZE // 2
        piece_y = y - SQUARE_SIZE // 2
        screen.blit(pieces[selected_piece], (piece_x, piece_y))
        
        # Remove a peça original do tabuleiro temporariamente
        board[selected_pos[0]][selected_pos[1]] = ''
    
    # Atualiza a tela para refletir as mudanças
    pygame.display.flip()