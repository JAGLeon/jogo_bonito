import pygame
from settings import *
from random import randint
from aleatorios import *

#Direcciones

DR = 3
UR = 9
DL = 1
UL = 7

rect = 0
color = 1
dir = 2

block_width = 100
block_height = 100


pygame.init()


SCREEN = pygame.display.set_mode(SIZE_SCREEN)
pygame.display.set_caption("Jogo bonito")

clock = pygame.time.Clock()


blocks= [
            {
                "rect":pygame.Rect(randint(0,WIDTH - block_width),randint(0,HEIGHT - block_height),block_width,block_height),
                "color":RED,
                "dir":DL,
                "borde":0,
                "radio":-1,
            },
            {
                "rect":pygame.Rect(randint(0,WIDTH - block_width),randint(0,HEIGHT - block_height),block_width,block_height),
                "color":GREEN,
                "dir":DR,
                "borde":0,
                "radio":-1,
            },
            {
                "rect":pygame.Rect(randint(0,WIDTH - block_width),randint(0,HEIGHT - block_height),block_width,block_height),
                "color":BLUE,
                "dir":UL,
                "borde":0,
                "radio":-1,
            },
        ]

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

    for block in blocks :
    #DIRECCION
        if block["rect"].right >= WIDTH:
            if block["dir"] == DR:
                block["dir"] = DL
            else:
                block["dir"] = UL
            block["color"] = get_random_color(colors)
        elif block["rect"].left <= 0:
            if block["dir"] == DL:
                block["dir"] = DR
            else:
                block["dir"] = UR
            block["color"] = random_color()
        elif block["rect"].bottom >= HEIGHT:
            if block["dir"] == DR:
                block["dir"] = UR
            else:
                block["dir"] = UL
            block["borde"] = randint(0,10)
        elif block["rect"].top <= 0:
            if block["dir"] == UR:
                block["dir"] = DR
            else:
                block["dir"] = DL
            block["radio"] = randint(-1,10)

        #MOVIMIENTOS
        if block["dir"] == DR:
            block["rect"].x += speed
            block["rect"].y += speed
        elif block["dir"] == DL:
            block["rect"].x -= speed
            block["rect"].y += speed
        elif block["dir"] == UL:
            block["rect"].x -= speed
            block["rect"].y -= speed
        elif block["dir"] == UR:
            block["rect"].x += speed
            block["rect"].y -= speed


    #dibujar pantalla
    SCREEN.fill(CUSTOM)
    for block in blocks:
        pygame.draw.rect(SCREEN, block["color"], block["rect"],block["borde"],block["radio"])

    #actualizar pantalla
    pygame.display.flip()

pygame.quit()



