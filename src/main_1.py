import pygame
from settings import *

pygame.init()


SCREEN = pygame.display.set_mode(SIZE_SCREEN)
pygame.display.set_caption("Jogo bonito")



clock = pygame.time.Clock()
block = pygame.Rect(0,0,200,100)
block.center = CENTER_SCREEN
speed = 5

# pygame.color.THECOLORS.items()

is_running = True
gravedad = True
gravedad_x = True


while is_running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    #actualizar elementos
    # if block.bottom <= HEIGHT:
    #     block.y += speed
    # if block.top <= HEIGHT:
    #     block.y += speed
    # else : 
    #     block.bottom = 0

    if gravedad:
        if block.bottom <= HEIGHT:
            block.y += speed
        else : 
            gravedad = False
    else : 
        if block.top >= 0:
            block.y -= speed
        else : 
            gravedad = True

    if gravedad_x:
        if block.right <= WIDTH:
            block.x += speed
        else : 
            gravedad_x = False
    else : 
        if block.left >= 0:
            block.x -= speed
        else : 
            gravedad_x = True

    
    #dibujar pantalla
    SCREEN.fill(CYAN)
    pygame.draw.rect(SCREEN, BLUE, block)

    #actualizar pantalla
    pygame.display.flip()

pygame.quit()

#hacer que rebote en el eje x
#tambien de forma diagonal

# pygame.rect.Rect()
# pygame.Rect()

    # pygame.draw.rect(SCREEN, RED, (100,0,200,100))
    # pygame.draw.rect(SCREEN, RED, (300,400,200,100),3)
    # pygame.draw.rect(SCREEN, RED, (WIDTH//2 - 200 //2 ,HEIGHT/2 - 100 /2,200,100),3,10)
    # pygame.draw.rect(SCREEN, BLUE, rect_1)
    # rect_2 = pygame.draw.circle(SCREEN, MAGENTA, (100,150),60)
    # pygame.draw.rect(SCREEN, BLUE, rect_2,2)
    # # pygame.draw.line(SCREEN, BLACK, (0,0),(800,600),3)
    # rect_3 = pygame.draw.line(SCREEN, BLACK, rect_2.center,rect_1.center,3)
    # pygame.draw.rect(SCREEN, CUSTOM, rect_3,2)

    # rect_4=pygame.draw.polygon(SCREEN, WHITE, [(100,100),(600,100),(230,200)],4)
    # pygame.draw.rect(SCREEN, CUSTOM, rect_4,2)

    # rect_5=pygame.draw.ellipse(SCREEN, BLACK,(300,400,100,150) ,4)