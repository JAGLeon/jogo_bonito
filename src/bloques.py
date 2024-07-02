import pygame
from settings import *
from random import randint

def crear_bloque(imagen:pygame.Surface = None,left = 0,top = 0,width = 50,height = 50,color = WHITE,dir = 3,borde = 0,radio = -1):
    if imagen:
        imagen = pygame.transform.scale(imagen, (width,height))

    return {
            "rect": pygame.Rect(left,top,width,height),
            "color": color,
            "dir": dir,
            "borde":borde,
            "radio":radio,
            "img": imagen
           }

def crear_coin(imagen:pygame.Surface = None):
    block = crear_bloque(imagen,randint(0,WIDTH - coin_w), randint(-HEIGHT,0 - coin_h), coin_w, coin_h, YELLOW, 0, 0, coin_h // 2)
    block["speed_y"] = randint(MIN_SPEED_Y_COIN,MAX_SPEED_Y_COIN)
    return block

def crear_player(imagen:pygame.Surface = None):
    return crear_bloque(imagen,randint(0,WIDTH - coin_w), randint(0,HEIGHT - coin_h), player_w, player_h, BLUE, 0, 0,0)

def cargar_coins(list,count_list,imagen:pygame.Surface = None):
    for _ in range(count_list):
        list.append(crear_coin(imagen))

def create_laser(midBottom:tuple[int,int],color:tuple[int,int,int] = RED):
    block = {"rect":pygame.Rect(0,0,LASER_WIDTH,LASER_HEIGHT),"color":color,"speed": LASER_SPEED}
    block["rect"].midbottom = midBottom
    return block
