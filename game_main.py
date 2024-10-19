import pygame
import sys
import random
from pygame.locals import *

def Move_Animation():
    if moving:
        animation_phase += animation_speed
        if animation_phase >= 360:
            animation_phase = 0
        scale_x = 0.8 + 0.5 * pygame.math.sin(pygame.math.radians(animation_phase))
        scale_y = 1.3 + 0.5 * pygame.math.sin(pygame.math.radians(animation_phase))

pygame.init()

animation_phase = 0 # Фаза анімації
animation_speed = 5 # Швидкість анімації

clock = pygame.time.Clock() # Додавання лічильника

# Розміри вікна
WIDTH, HEIGHT = 800, 600 # Ширина і висота
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Їстівна планета")

# Колір фону
background_color = (255, 255, 255)
background_color_2 = '#B6FEFF'

# Колір і розмір слайма
SLIME_COLOR = (0, 255, 0)
SLIME_RADIUS = 20

# Початкова позиція слайма (центр екрану)
slime_x, slime_y = WIDTH // 2, HEIGHT // 2

# Завантаження спрайту слайма
slime_image = pygame.image.load('slime.png').convert_alpha()

# Масштабування спрайта до бажаного розміру
slime_size = 60
slime_image = pygame.transform.scale(
    slime_image, # посилання на зображення
    (slime_size, slime_size)) # розмір по осям "x" та "y"

# Початковий напрямок
direction = 0 # Кут в градусах

# Швидкість слайма
SPEED = 5

# Основний ігровий цикл
running = True
while running:
    # Заповнює екранний простір кольором фону
    screen.fill(background_color_2)

    clock.tick(60) # Обмежує кількість кадрів на секунду

    # Основний обробник подій
    for event in pygame.event.get(): # Перебирає події
        if event.type == pygame.QUIT: # Якщо подія - Вихід
            running = False # Перериває виконання основного ігрового циклу

    # Отримання стану клавіш
    keys = pygame.key.get_pressed()

    # Визначення напрямку
    moving = False
    dx, dy = 0, 0

    # Рух на WASD у восьми напрямках
    if keys[pygame.K_w] and keys[pygame.K_a]:
        dx = -SPEED // 1.414
        dy = -SPEED // 1.414
        direction = 225
        moving = True
    elif keys[pygame.K_w] and keys[pygame.K_d]:
        dx = SPEED // 1.414
        dy = -SPEED // 1.414
        direction = 315
        moving = True
    elif keys[pygame.K_s] and keys[pygame.K_a]:
        dx = -SPEED // 1.414
        dy = SPEED // 1.414
        direction = 135
        moving = True
    elif keys[pygame.K_s] and keys[pygame.K_d]:
        dx = SPEED // 1.414
        dy = SPEED // 1.414
        direction = 45
        moving = True

    elif keys[pygame.K_w] or keys[pygame.K_UP]:
        dy = -SPEED
        direction = 270
        moving = True
    elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
        dy = SPEED
        direction = 90
        moving = True
    elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
        dx = -SPEED
        direction = 180
        moving = True
    elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        dx = SPEED
        direction = 0
        moving = True

    # Оновлення позиції слайма
    slime_x += dx
    slime_y += dy

    # Обертання спрайта у напрямку руху
    if moving:
        rotated_slime = pygame.transform.rotate(slime_image, -direction)
    # Без обертання,якщо не рухається
    else:
        rotated_slime = slime_image
        
    # отримуємо прямокутник спрайта
    slime_rect = rotated_slime.get_rect(center=(slime_x, slime_y))
    # Малювання спрайта на екрані
    screen.blit(rotated_slime, slime_rect)

    # Оновлення дисплею
    pygame.display.flip()

pygame.quit() # Вимикає вікно pygame

