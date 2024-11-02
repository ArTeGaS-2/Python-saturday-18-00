import pygame
import sys
import random
from pygame.locals import *

# Розміри вікна
WIDTH, HEIGHT = 800, 600 # Ширина і висота
# Колір фону
background_color = (255, 255, 255)
background_color_2 = '#B6FEFF'
# Масштабування спрайта до бажаного розміру
slime_size = 60
# Швидкість слайма
SPEED = 5
ANIMATTION_SPEED = 0.1



def init_game():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Їстівна планета")
    return screen



def load_slime_image():
    # Завантаження спрайту слайма
    slime_image = pygame.image.load('slime.png').convert_alpha()

    return pygame.transform.scale(
    slime_image, # посилання на зображення
    (slime_size, slime_size)) # розмір по осям "x" та "y"

def slime_movemet(keys, slime_x, slime_y, SPEED, direction):
    # Визначення напрямку
    moving = False
    dx, dy = 0, 0

    # Рух на WASD у восьми напрямках
    if keys[pygame.K_w] and keys[pygame.K_a]:
        dx = -SPEED // 1.414
        dy = -SPEED // 1.414
        direction = 135
        moving = True
    elif keys[pygame.K_w] and keys[pygame.K_d]:
        dx = SPEED // 1.414
        dy = -SPEED // 1.414
        direction = 45
        moving = True
    elif keys[pygame.K_s] and keys[pygame.K_a]:
        dx = -SPEED // 1.414
        dy = SPEED // 1.414
        direction = 225
        moving = True
    elif keys[pygame.K_s] and keys[pygame.K_d]:
        dx = SPEED // 1.414
        dy = SPEED // 1.414
        direction = 315
        moving = True

    elif keys[pygame.K_w] or keys[pygame.K_UP]:
        dy = -SPEED
        direction = 90
        moving = True
    elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
        dy = SPEED
        direction = 270
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

    return slime_x, slime_y, direction, moving

def lerp(a,b,t):
    """ Лінійна інтероляція між "a" та "b" з коефіцієнт "t". """
    return a + (b - a) * t

def animate_slime(moving, direction, slime_image, slime_x, slime_y,
                  current_scale_x, current_scale_y):
    if moving:
        if direction in [0, 180]: # Горизонтальний рух
            target_scale_x, target_scale_y = 1.3, 0.8
        elif direction in [90, 270]: # Вертикальний рух
            target_scale_x, target_scale_y = 1.3, 0.8
        else: # Діагональний рух
            target_scale_x, target_scale_y = 1.3, 0.8
    else:
        target_scale_x, target_scale_y = 1.0, 1.0
    # Поступове оновлення масштабів за допомогою lerp
    new_scale_x = lerp(current_scale_x, target_scale_x, ANIMATTION_SPEED)
    new_scale_y = lerp(current_scale_y, target_scale_y, ANIMATTION_SPEED)
    
    # Спочатку масштабування
    scaled_image = pygame.transform.scale(
        slime_image,(int(slime_size * new_scale_x),
                     int(slime_size * new_scale_y)))
    
    # Потім обертання
    if direction is not None:
        rotated_slime = pygame.transform.rotate(scaled_image, direction)
    else:
        rotated_slime = scaled_image
    slime_rect = rotated_slime.get_rect(center=(slime_x, slime_y))
    return rotated_slime, slime_rect, new_scale_x, new_scale_y
    
# Ініціалізація гри
screen = init_game()
slime_image = load_slime_image()
clock = pygame.time.Clock() # Додавання лічильника
# Початкова позиція слайма (центр екрану)
slime_x, slime_y = WIDTH // 2, HEIGHT // 2
running = True

current_scale_x = 1.0
current_scale_y = 1.0
direction = 0 # Кут в градусах
# Основний ігровий цикл
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

    slime_x, slime_y, direction, moving = slime_movemet(
        keys, slime_x, slime_y, SPEED, direction)
    slime, slime_rect, current_scale_x, current_scale_y = animate_slime(
        moving, direction, slime_image, slime_x, slime_y,
        current_scale_x, current_scale_y)

    # Малювання спрайта на екрані
    screen.blit(slime, slime_rect)

    # Оновлення дисплею
    pygame.display.flip()

pygame.quit() # Вимикає вікно pygame

