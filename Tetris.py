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

def create_new_piece():
    """Створює нову випадкову фігуру на старті зверху"""
    fig_idx = random.randrange(len(FIGURES)) # індекс фігури
    shape = [row[:] for row in FIGURES[fig_idx]] # Копія фігури
    x_start = FIELD_WIDTH // 2 - len(shape[0]) // 2 # центр по ширині
    y_start = 0 # а у меня встал(внизу)
    return [shape, fig_idx, x_start, y_start]

def is_collision(piece, dx, dy):
    """Перевіряє: якщо зсунемо фігуру на dx,dy - на врізання"""
    shape, idx, px, py = piece # розпаковка списку
    for row_i, row in enumerate(shape):
        for col_i, cell in enumerate(row):
            if cell:
                x = px + col_i + dx
                y = py + row_i + dy
                if x < 0 or x >= FIELD_WIDTH:
                    return True
                if y >= FIELD_HEIGHT:
                    return True
                if y >= 0 and field[y][x]:
                    return True
    return False

def place_piece(piece):
    """Прикріплює фігуру до поля"""
    shape, idx, px, py = piece
    for r, row in enumerate(shape):
        for c, cell in enumerate(row):
            if cell:
                x = px + c
                y = py + r
                if 0 <= x < FIELD_WIDTH and 0 <= y < FIELD_HEIGHT:
                    field[y][x] = idx + 1

def clear_full_lines():
    """Видаляє повні рядки та додає звурху порожні"""
    global field
    field = [row for row in field if 0 in row]
    while len(field) < FIELD_HEIGHT:
        field.insert(0, [0]*FIELD_WIDTH)

def rotate_piece(piece):
    """Обертає фігуру на 90° (за годинниковою стрілкою)"""
    shape, idx, px, py = piece
    rotated = [list(col) for col in zip(*shape[::-1])]
    return [rotated, idx, px, py]

# ----------------- Ініціалізація Pygame -----------------
pygame.init()
screen = pygame.display.set_mode((FIELD_WIDTH*CELL_SIZE,
                                  FIELD_HEIGHT*CELL_SIZE))
pygame.display.set_caption("Тетріс")
clock = pygame.time.Clock()

current = create_new_piece()

fall_timer = 0
game_over = False
# ----------------- Основний цикл гри -----------------

while True:
    # Якщо гра завершилась - трохи чекаємо і виходимо
    if game_over:
        pygame.time.wait(2000)
        break
    # Обробка подій (клавіші, вихід)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and not is_collision(    
                current, -1, 0):
                current[2] -= 1 # Рух ліворуч
            elif event.key == pygame.K_RIGHT and not is_collision(    
                current, 1, 0):
                current[2] += 1 # Рух праворуч
            elif event.key == pygame.K_DOWN and not is_collision(    
                current, 0, 1):
                current[3] += 1 # "Швидке" падіння
            elif event.key == pygame.K_UP:
                rotated = rotate_piece(current)
                if not is_collision(rotated, 0, 0):
                    current = rotated
    
    fall_timer += clock.get_time()
    clock.tick(60)

    if fall_timer >= FALL_DELAY:
        if not is_collision(current, 0, 1):
            current[3] += 1 # опускаємо фігуру
        else: 
            place_piece(current) # закріплюємо
            clear_full_lines() # перевіряємо на заповнені лінії
            current = create_new_piece() # нова фігура
            if is_collision(current, 0,0):
                game_over = True
        fall_timer = 0
    
    screen.fill((20,20,20)) # Фон

    # Малюємо всі встановлені фігури
    for y, row in enumerate(field):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen,
                    COLORS[cell-1],
                    (x*CELL_SIZE,y*CELL_SIZE,CELL_SIZE,CELL_SIZE))
    
    shape, idx, px, py = current
    for r, row in enumerate(shape):
        for c, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, COLORS[idx],
                    ((px+c)*CELL_SIZE, (py+r)*CELL_SIZE,
                     CELL_SIZE, CELL_SIZE))
    pygame.display.flip()
    

