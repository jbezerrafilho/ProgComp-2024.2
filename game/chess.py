import pygame
from setup import setup_game
from events import handle_events
from draw import render  

def main():
    # Inicializa o jogo
    screen, pieces, board, SQUARE_SIZE, ROWS, COLS, LIGHT_COLOR, DARK_COLOR, error_sound, success_sound = setup_game()

    # Variáveis de controle de estado
    selected_piece, selected_pos, dragging, running = None, None, False, True
    
    # Loop principal do Jogo
    while running:
        running, selected_piece, selected_pos, dragging = handle_events(board, selected_piece, selected_pos, dragging, success_sound, error_sound, SQUARE_SIZE)
        render(screen, board, pieces, SQUARE_SIZE, ROWS, COLS, LIGHT_COLOR, DARK_COLOR, selected_piece, selected_pos, dragging)

    pygame.quit()

main()