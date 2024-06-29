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
count_blocks = 2 


pygame.init()


SCREEN = pygame.display.set_mode(SIZE_SCREEN)
pygame.display.set_caption("Jogo bonito")

clock = pygame.time.Clock()

def detectar_colision(block_1,block_2):
    if  punto_en_rectangulo(block_1.topleft,block_2) or \
        punto_en_rectangulo(block_1.topright,block_2) or \
        punto_en_rectangulo(block_1.bottomleft,block_2) or \
        punto_en_rectangulo(block_1.bottomleft,block_2) or \
        punto_en_rectangulo(block_2.topleft,block_1) or \
        punto_en_rectangulo(block_2.topright,block_1) or \
        punto_en_rectangulo(block_2.bottomleft,block_1) or \
        punto_en_rectangulo(block_2.bottomleft,block_1):
        return True
    else: 
        return False

def punto_en_rectangulo(punto,rect):
    coordenada_x, coordenada_y = punto
    return rect.left <= coordenada_x and rect.right >= coordenada_x and rect.top <= coordenada_y and rect.bottom >= coordenada_y

def crear_bloque(left = 0,top = 0,width = 50,height = 50,color = WHITE,dir = 3,borde = 0,radio = -1):
    return {
            "rect": pygame.Rect(left,top,width,height),
            "color": color,
            "dir": dir,
            "borde":borde,
            "radio":radio,
           }


blocks = []

for block in range(count_blocks):
    blocks.append(crear_bloque(randint(100,500)))

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

    if detectar_colision(blocks[0]["rect"],blocks[1]["rect"]):
        print("Colision")

    #dibujar pantalla
    SCREEN.fill(CUSTOM)
    for block in blocks:
        pygame.draw.rect(SCREEN, block["color"], block["rect"],block["borde"],block["radio"])

    #actualizar pantalla
    pygame.display.flip()

pygame.quit()



