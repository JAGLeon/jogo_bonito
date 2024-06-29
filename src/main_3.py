import pygame
from settings import *

#Direcciones

DR = 3
UR = 9
DL = 1
UL = 7

rect = 0
color = 1
dir = 2

pygame.init()


SCREEN = pygame.display.set_mode(SIZE_SCREEN)
pygame.display.set_caption("Jogo bonito")

clock = pygame.time.Clock()


block = [pygame.Rect(300,250,200,100),RED,DL]
block_2 = [pygame.Rect(240,120,200,100),RED,DL]

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
    if block[rect].right >= WIDTH:
        if block[dir] == DR:
            block[dir] = DL
        else:
            block[dir] = UL
    elif block[rect].left <= 0:
        if block[dir] == DL:
            block[dir] = DR
        else:
            block[dir] = UR
    elif block[rect].bottom >= HEIGHT:
        if block[dir] == DR:
            block[dir] = UR
        else:
            block[dir] = UL
    elif block[rect].top <= 0:
        if block[dir] == UR:
            block[dir] = DR
        else:
            block[dir] = DL

    #MOVIMIENTOS
    if block[dir] == DR:
        block[rect].x += speed
        block[rect].y += speed
    elif block[dir] == DL:
        block[rect].x -= speed
        block[rect].y += speed
    elif block[dir] == UL:
        block[rect].x -= speed
        block[rect].y -= speed
    elif block[dir] == UR:
        block[rect].x += speed
        block[rect].y -= speed


    #dibujar pantalla
    SCREEN.fill(CYAN)
    pygame.draw.rect(SCREEN, block[color], block[rect])

    #actualizar pantalla
    pygame.display.flip()

pygame.quit()



