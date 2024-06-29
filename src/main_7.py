import pygame
from settings import *
from random import randint
from aleatorios import *

#Direcciones

DR = 3
UR = 9
DL = 1
UL = 7

block_width = 50
block_height = 50
count_coins = 25
coin_w = 20
coin_h = 20


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


block = crear_bloque(randint(0,WIDTH - block_width), randint(0,HEIGHT - block_height), block_width, block_height,dir = 7,color = randint(0, WIDTH - block_width))

coins = []

def cargar_coins():
    for i in range(count_coins):
        coins.append(crear_bloque(randint(0,WIDTH - coin_w), randint(0,HEIGHT - coin_h), coin_w, coin_h, YELLOW, 0, 0, coin_h // 2))

cargar_coins()

font = pygame.font.Font(None, 36)
is_running = True
gravedad = True
gravedad_x = True
coins_colision = 0


while is_running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

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
        block["rect"].x += SPEED
        block["rect"].y += SPEED
    elif block["dir"] == DL:
        block["rect"].x -= SPEED
        block["rect"].y += SPEED
    elif block["dir"] == UL:
        block["rect"].x -= SPEED
        block["rect"].y -= SPEED
    elif block["dir"] == UR:
        block["rect"].x += SPEED
        block["rect"].y -= SPEED

    for coin in coins[:]:
        if detectar_colision(coin["rect"],block["rect"]):
            coins.remove(coin)
            coins_colision += 1

    if len(coins) == 0:
        cargar_coins()

    #dibujar pantalla
    SCREEN.fill(BLACK)
    pygame.draw.rect(SCREEN, block["color"], block["rect"],block["borde"],block["radio"])

    for coin in coins:
        pygame.draw.rect(SCREEN, coin["color"], coin["rect"],coin["borde"],coin["radio"])

    text = font.render(f"Coins colisionados: {coins_colision}", True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, 20))
    SCREEN.blit(text,text_rect.topleft)
    #actualizar pantalla
    pygame.display.flip()

pygame.quit()



