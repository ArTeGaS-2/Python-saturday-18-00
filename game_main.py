import pygame

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

    
    # Малювання слайма
    pygame.draw.circle(
        screen, # Поверхня
        SLIME_COLOR, # Колір
        (slime_x, slime_y), # Координати
        SLIME_RADIUS) # Розмір

    # Оновлення дисплею
    pygame.display.flip()

pygame.quit() # Вимикає вікно pygame

