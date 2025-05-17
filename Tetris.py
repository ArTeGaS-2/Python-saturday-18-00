import pygame
import sys
import random

# ----------------- Налаштування гри -----------------
# Розмір поля в клітинках
FIELD_WIDTH, FIELD_HEIGHT = 10, 20  
# Розмір однієї клітинки в пікселях
CELL_SIZE = 30  
# Швидкість падіння (мс між кроками вниз)
FALL_DELAY = 500  

# Ініціалізуємо порожнє поле: 0 – порожньо, >0 – зайнято фігурою
field = [[0 for i in range(
    FIELD_WIDTH)] for i in range(FIELD_HEIGHT)]

# Матриці всіх 7 фігур тетрісу (1 – зайнято, 0 – порожньо)
FIGURES = [
    [[1, 1, 1, 1]],                # I-лінія
    [[1, 1], [1, 1]],              # O-квадрат
    [[0, 1, 0], [1, 1, 1]],        # T-тетріс
    [[1, 0, 0], [1, 1, 1]],        # J
    [[0, 0, 1], [1, 1, 1]],        # L
    [[1, 1, 0], [0, 1, 1]],        # S
    [[0, 1, 1], [1, 1, 0]],        # Z
]
# Відповідні кольори (RGB) для кожної фігури
COLORS = [
    (0, 240, 240),   # I – блакитний
    (240, 240, 0),   # O – жовтий
    (160, 0, 240),   # T – фіолетовий
    (0, 0, 240),     # J – синій
    (240, 160, 0),   # L – помаранчевий
    (0, 240, 0),     # S – зелений
    (240, 0, 0),     # Z – червоний
]
# ----------------- Функції для логіки -----------------
# ----------------- Ініціалізація Pygame -----------------
pygame.init()
screen = pygame.display.set_mode((FIELD_WIDTH*CELL_SIZE,
                                  FIELD_HEIGHT*CELL_SIZE))
pygame.display.set_caption("Тетріс")
clock = pygame.time.Clock()

current_piece = new_piece()
fall_timer = 0
game_over = False
# ----------------- Основний цикл гри -----------------

while True:
    # Якщо гра завершилась - трохи чекаємо і виходимо
    if game_over:
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()
    # Обробка подій (клавіші, вихід)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
