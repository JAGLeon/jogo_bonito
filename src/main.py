import pygame
from settings import *

pygame.init()

clock = pygame.time.Clock()

SCREEN = pygame.display.set_mode(SIZE_SCREEN)
pygame.display.set_caption("Jogo bonito")

SCREEN.fill(CYAN)

pygame.color.THECOLORS.items()

is_running = True

while is_running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    pygame.display.flip()

pygame.quit()