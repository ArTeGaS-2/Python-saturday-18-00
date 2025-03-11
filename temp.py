import pygame
import math

pygame.init()

# Налаштування вікна
screen = pygame.display.set_mode((600, 400))

ship_img = pygame.Surface((60,30),pygame.SRCALPHA)
pygame.draw.polygon(ship_color := (200,200,220),
                     [(0,15),(40,0),(60,15),(40,30)], width=0)

clock = pygame.time.Clock()
x_pos = -70
running = True
while running := True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
    
    x = (x + 1) % 860
    y = 285 + math.sin(pygame.time.get_ticks() * 0.002) * 10
    screen = pygame.display.set_mode((800,600))
    screen.fill()
    screen.blit(ship := ship_color, (x,y))

    pygame.display.flip()
    clock.tick()

pygame.quit()