import pygame
from setup import setup_game
from events import handle_events
from draw import render

def main():
    # Inicializa o jogo
    game_state = setup_game()

    # Loop principal do Jogo
    while game_state['running']:
        # Processa eventos do jogo
        game_state = handle_events(game_state)
        
        # Renderiza o tabuleiro e as peças
        render(game_state)

    pygame.quit()

main()