import pygame

def draw_board(screen, rows, cols, square_size, light_color, dark_color):
    """Desenha o tabuleiro."""
    for row in range(rows):
        for col in range(cols):
            color = light_color if (row + col) % 2 == 0 else dark_color
            pygame.draw.rect(screen, color, (col * square_size, row * square_size, square_size, square_size))

def draw_pieces(screen, board, pieces, square_size):
    """Desenha as peças no tabuleiro."""
    for row in range(len(board)):
        for col in range(len(board[row])):
            piece = board[row][col]  # Obtém a peça na posição (row, col)
            if piece:  # Se houver uma peça na posição
                # Desenha a imagem da peça no centro do quadrado
                screen.blit(pieces[piece], (col * square_size, row * square_size))

def render(screen, board, pieces, SQUARE_SIZE, ROWS, COLS, LIGHT_COLOR, DARK_COLOR, selected_piece, selected_pos, dragging):
    # Renderiza o tabuleiro e as peças
    draw_board(screen, ROWS, COLS, SQUARE_SIZE, LIGHT_COLOR, DARK_COLOR)
    draw_pieces(screen, board, pieces, SQUARE_SIZE)
    if dragging and selected_piece:
        mouse_pos = pygame.mouse.get_pos()
        x, y = mouse_pos
        # Desenha a peça sendo arrastada na posição do mouse
        screen.blit(pieces[selected_piece], (x - SQUARE_SIZE // 2, y - SQUARE_SIZE // 2))
        # Remove a peça original do tabuleiro temporariamente
        board[selected_pos[0]][selected_pos[1]] = ''
    pygame.display.flip()