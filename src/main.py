import pygame
from settings import *
from random import randint
from aleatorios import *
from bloques import *
from colisiones import *
from pygame.locals import *
import sys

def mostrar_texto(superficie:pygame.Surface,coordenada:tuple[int,int] ,texto:str,fuente:pygame.font,color:tuple[int,int,int] = WHITE,bg:tuple[int,int,int] = BLACK):
    sup_text = fuente.render(texto,True,color,bg)
    rect_texto = sup_text.get_rect()
    rect_texto.center = coordenada

    superficie.blit(sup_text,rect_texto)

def wait_user(tecla):
    flag_start = True
    while flag_start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == tecla:
                    flag_start = False

#img 
img_ovni = pygame.image.load("./src/assets/ovni.png")
img_fondo = pygame.image.load("./src/assets/fondo.jpg")
img_asteroide = pygame.image.load("./src/assets/asteroide.png")
img_asteroide_2 = pygame.image.load("./src/assets/asteroide2.png")
img_fondo = pygame.image.load("./src/assets/fondo.jpg")
img_fondo = pygame.transform.scale(img_fondo,SIZE_SCREEN)

NEWCOINEVENT = USEREVENT + 1
TIMEOUT = USEREVENT + 2

#Direcciones
move_left = True
move_right = True
move_up = True
move_down = True

pygame.init()


SCREEN = pygame.display.set_mode(SIZE_SCREEN)
pygame.display.set_caption("Jogo bonito")

clock = pygame.time.Clock()

block = crear_player(img_ovni)
coins = []

cargar_coins(coins,INITIAL_COINS,img_asteroide_2)

font = pygame.font.Font(None, 36)
coins_colision = 0
score_text = font.render(f"Coins colisionados: {coins_colision}",True,BLUE)
is_running = True
counter_colision = 0

#cargo sonido
pygame.mixer.init()
colision_sonido = pygame.mixer.Sound("./src/assets/coin.mp3")
exito_sonido = pygame.mixer.Sound("./src/assets/exito.mp3")
gamer_over_sonido = pygame.mixer.Sound("./src/assets/game_over.mp3")

playing_music = True
pygame.time.set_timer(NEWCOINEVENT,5000)

SCREEN.fill(BLACK)
mostrar_texto(SCREEN,CENTER_SCREEN,"Asteroides",font,RED)
mostrar_texto(SCREEN,(WIDTH // 2,HEIGHT - 50),"Presiones espacio para comenzar",font,BLUE)
pygame.display.flip()
wait_user(K_SPACE)
#musica para todo el juego
pygame.mixer.music.load("./src/assets/musica_fondo.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play()

pygame.time.set_timer(TIMEOUT,30000,1)

while is_running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                move_down = True
                move_up = False
            if event.key == K_UP:
                move_up = True
                move_down = False
            if event.key == K_LEFT:
                move_left = True
                move_right = False
            if event.key == K_RIGHT:
                move_right = True
                move_left = False
            if event.key == K_m:
                if playing_music:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
                playing_music = not playing_music

        if event.type == KEYUP:
            if event.key == K_DOWN:
                move_down = False
            if event.key == K_UP:
                move_up = False
            if event.key == K_LEFT:
                move_left = False
            if event.key == K_RIGHT:
                move_right = False

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                new_coin = crear_coin()
                new_coin["color"] = MAGENTA
                new_coin["rect"].center = event.pos
                coins.append(new_coin)

        if event.type == NEWCOINEVENT:
                new_coin = crear_coin()
                new_coin["color"] = RED
                coins.append(new_coin)

        if event.type == TIMEOUT:
            is_running = False

    if move_left and block["rect"].left > 0:
        block["rect"].x -= SPEED
        if block["rect"].left < 0:
            block["rect"].left = 0
    if move_right and block["rect"].right < WIDTH:
        block["rect"].x += SPEED
        if block["rect"].right > WIDTH:
            block["rect"].right = WIDTH
    if move_up and block["rect"].top > 0:
        block["rect"].y -= SPEED
        if block["rect"].top < 0:
            block["rect"].top = 0
    if move_down and block["rect"].bottom < HEIGHT:
        block["rect"].y += SPEED
        if block["rect"].bottom > HEIGHT:
            block["rect"].bottom = HEIGHT


    for coin in coins[:]:
        if detectar_colision_circulos(coin["rect"],block["rect"]):
            colision_sonido.play()
            counter_colision = 10
            coins.remove(coin)
            coins_colision += 1
            score_text = font.render(f"Coins colisionados: {coins_colision}",True,BLUE)
            if len(coins) == 0:
                exito_sonido.play()
                cargar_coins(coins,INITIAL_COINS,img_asteroide)

    if counter_colision > 10:
        counter_colision -= 1
        block["rect"].width = player_w + 5

    #dibujar pantalla
    SCREEN.blit(img_fondo, (0,0))

    SCREEN.blit(block["img"],block["rect"])


    for coin in coins:
        if coin["img"]:
            SCREEN.blit(coin["img"],coin["rect"])
        else:    
            pygame.draw.rect(SCREEN, coin["color"], coin["rect"],coin["borde"],coin["radio"])

    mostrar_texto(SCREEN,POSICION_SCORE, f"Score: {coins_colision}",font,BLUE)
    #actualizar pantalla
    pygame.display.flip()


#pantalla fin
pygame.mixer.music.stop()
gamer_over_sonido.play()
SCREEN.fill(BLACK)
mostrar_texto(SCREEN,CENTER_SCREEN,"GAME OVER",font,RED)
mostrar_texto(SCREEN,(WIDTH // 2,HEIGHT - 50),"Presiones espacio para comenzar",font,BLUE)
pygame.display.flip()
wait_user(K_SPACE)

pygame.quit()



