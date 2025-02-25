import pygame

# Inicializa o Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# Cores
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
WHITE = (232, 235, 239)   # um tom claro (por ex. quase branco)
GREY  = (125, 135, 150)   # um tom escuro  (por ex. cinza azulado)

# Tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Xadrez")

def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE if (row + col) % 2 == 0 else GREY
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_board()
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()