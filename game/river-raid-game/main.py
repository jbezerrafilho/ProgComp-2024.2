import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("River Raid")

# Cores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Configurações do jogador
player_width = 40
player_height = 60
player_x = SCREEN_WIDTH // 2 - player_width // 2
player_y = SCREEN_HEIGHT - player_height - 20
player_speed = 5

# Configurações dos inimigos
enemy_width = 40
enemy_height = 40
enemies = []
enemy_speed = 3

# Clock para controlar FPS
clock = pygame.time.Clock()

# Loop principal do jogo
running = True
while running:
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Movimentação do jogador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_width:
        player_x += player_speed
    
    # Gerar inimigos
    if len(enemies) < 5 and random.randint(0, 100) < 2:
        enemy_x = random.randint(0, SCREEN_WIDTH - enemy_width)
        enemies.append([enemy_x, -enemy_height])
    
    # Atualizar posição dos inimigos
    for enemy in enemies[:]:
        enemy[1] += enemy_speed
        if enemy[1] > SCREEN_HEIGHT:
            enemies.remove(enemy)
    
    # Limpar a tela
    screen.fill(WHITE)
    
    # Desenhar o rio
    pygame.draw.rect(screen, BLUE, (100, 0, SCREEN_WIDTH - 200, SCREEN_HEIGHT))
    
    # Desenhar o jogador
    pygame.draw.rect(screen, GREEN, (player_x, player_y, player_width, player_height))
    
    # Desenhar os inimigos
    for enemy in enemies:
        pygame.draw.rect(screen, (255, 0, 0), (enemy[0], enemy[1], enemy_width, enemy_height))
    
    # Atualizar a tela
    pygame.display.flip()
    
    # Controlar FPS
    clock.tick(60)

pygame.quit()