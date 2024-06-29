import pygame
from settings import *

#Direcciones

DR = 3
UR = 9
DL = 1
UL = 7


pygame.init()


SCREEN = pygame.display.set_mode(SIZE_SCREEN)
pygame.display.set_caption("Jogo bonito")

clock = pygame.time.Clock()


block = pygame.Rect(300,250,200,100)
block_dir = DR
block_color = RED

block_2 = pygame.Rect(240,120,200,100)
block_dir_2 = DL
block_color = RED

# pygame.color.THECOLORS.items()

speed = 5
is_running = True
gravedad = True
gravedad_x = True


while is_running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    #DIRECCION
    if block.right >= WIDTH:
        if block_dir == DR:
            block_dir = DL
        else:
            block_dir = UL
    elif block.left <= 0:
        if block_dir == DL:
            block_dir = DR
        else:
            block_dir = UR
    elif block.bottom >= HEIGHT:
        if block_dir == DR:
            block_dir = UR
        else:
            block_dir = UL
    elif block.top <= 0:
        if block_dir == UR:
            block_dir = DR
        else:
            block_dir = DL

    #MOVIMIENTOS
    if block_dir == DR:
        block.x += speed
        block.y += speed
    elif block_dir == DL:
        block.x -= speed
        block.y += speed
    elif block_dir == UL:
        block.x -= speed
        block.y -= speed
    elif block_dir == UR:
        block.x += speed
        block.y -= speed


    #dibujar pantalla
    SCREEN.fill(CYAN)
    pygame.draw.rect(SCREEN, block_color, block)

    #actualizar pantalla
    pygame.display.flip()

pygame.quit()

