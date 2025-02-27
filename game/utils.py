import pygame

def get_square_under_mouse(SQUARE_SIZE):
    mouse_pos = pygame.mouse.get_pos()
    x, y = mouse_pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col