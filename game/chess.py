import pygame
from pieces import load_pieces, initial_board  
from draw import draw_board, draw_pieces  
from utils import get_square_under_mouse  
from setup import setup_game

def main():

    # Inicializa o jogo
    screen, pieces, board, SQUARE_SIZE, ROWS, COLS, LIGHT_COLOR, DARK_COLOR, error_sound, success_sound = setup_game()

    # Variáveis de controle de estado
    selected_piece, selected_pos, dragging, running = None, None, False, True
    
    # Loop principal do Jogo
    while running:

        # Tratamento de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                row, col = get_square_under_mouse(SQUARE_SIZE)  # Obtém a posição do quadrado sob o cursor do mouse
                if board[row][col] != '':                       # Verifique se o quadrado contém peça
                    selected_piece = board[row][col]            # Armazene a peça'
                    selected_pos = (row, col)                   # Armazene a posição da peça
                    dragging = True                             # Peça sendo arrastada, isso permite que outras partes do código
                    
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
                                success_sound.play() 
                                board[row][col] = selected_piece                          
                                board[selected_pos[0]][selected_pos[1]] = ''
                            else:
                                # Se a peça for da mesma cor, alerte o usuario e restaura a peça original
                                error_sound.play()
                                board[selected_pos[0]][selected_pos[1]] = selected_piece
                        selected_piece = None
                        selected_pos = None
                        dragging = False

        # Rendereiza o tabuleiro e as peças
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

    pygame.quit()

main()