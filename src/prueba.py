import pygame
from settings_2 import *
from random import randint

is_running = True
clock = pygame.time.Clock()
screen = pygame.display.set_mode(SIZE_SCREEN)


puntos_count = 60

coor_list = []
for i in range(puntos_count):
    x = randint(0,WIDTH)
    y = randint(0,HEIGHT)
    coor_list.append([x,y])

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    screen.fill(BLACK)

    for coordenada in coor_list:
        pygame.draw.circle(screen, WHITE, coordenada, 2)
        coordenada[1] += 1
        if coordenada[1] >= HEIGHT:
            coordenada[1] = 0

    pygame.display.flip()
    clock.tick(FPS)



ceo 

CEO

DASCEO

DAACEO


DAAAAceo