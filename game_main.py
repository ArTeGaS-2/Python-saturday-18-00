import pygame
import sys
import random
from pygame.locals import *

pygame.init()

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
slime_size = 40
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

    # Рух на WASD у восьми напрямках
    if keys[pygame.K_w] and keys[pygame.K_a]:
        slime_x -= SPEED // 1.414
        slime_y -= SPEED // 1.414
    elif keys[pygame.K_w] and keys[pygame.K_d]:
        slime_x += SPEED // 1.414
        slime_y -= SPEED // 1.414
    elif keys[pygame.K_s] and keys[pygame.K_a]:
        slime_x -= SPEED // 1.414
        slime_y += SPEED // 1.414
    elif keys[pygame.K_s] and keys[pygame.K_d]:
        slime_x += SPEED // 1.414
        slime_y += SPEED // 1.414

    elif keys[pygame.K_w] or keys[pygame.K_UP]:
        slime_y -= SPEED
    elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
        slime_y += SPEED
    elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
        slime_x -= SPEED
    elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        slime_x += SPEED

    def draw_circle():
        # Малювання слайма
        pygame.draw.circle(
            screen, # Поверхня
            SLIME_COLOR, # Колір
            (slime_x, slime_y), # Координати
            SLIME_RADIUS) # Розмір
        
    # отримуємо прямокутник спрайта
    slime_rect = slime_image.get_rect(center=(slime_x, slime_y))
    # Малювання спрайта на екрані
    screen.blit(slime_image, slime_rect)

    # Оновлення дисплею
    pygame.display.flip()

pygame.quit() # Вимикає вікно pygame

