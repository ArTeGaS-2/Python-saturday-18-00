import pygame   # ⚙️ бібліотека для графіки і звуків
import sys      # ⚙️ завершення програми на будь‑якій ОС
import random   # ⚙️ випадкові числа/вибір (щоб випадково давати фігури)

# =============== 2. Налаштування гри =================
FIELD_WIDTH  = 10   # ширина поля у «клітинках» (1 клітинка = 1 блок фігури)
FIELD_HEIGHT = 20   # висота поля
CELL_SIZE    = 30   # розмір однієї клітинки на екрані в пікселях
FALL_DELAY   = 500  # мілісекунди між автоматичними кроками падіння фігури

# ------- Створюємо порожнє поле (таблицю з нулями) -------
# Поле виглядає так: [[0,0,0,...,0],  ← рядок 0 (верхній)
#                     [0,0,0,...,0],  ← рядок 1
#                     ...
#                     [0,0,0,...,0]] ← рядок 19 (дно)
field = [[0 for _ in range(
    FIELD_WIDTH)] for _ in range(FIELD_HEIGHT)]

# ------- Опис семи фігур Тетрісу та їх кольорів -------
FIGURES = [
    [[1,1,1,1]],           # I — довга лінія
    [[1,1], [1,1]],        # O — квадрат 2×2
    [[0,1,0], [1,1,1]],    # T
    [[1,0,0], [1,1,1]],    # J
    [[0,0,1], [1,1,1]],    # L
    [[1,1,0], [0,1,1]],    # S
    [[0,1,1], [1,1,0]]     # Z
]
# Кожен індекс FIGURES відповідає індексу COLORS
COLORS = [
    (0,240,240),  # I — блакитний
    (240,240,0),  # O — жовтий
    (160,0,240),  # T — фіолетовий
    (0,0,240),    # J — синій
    (240,160,0),  # L — помаранчевий
    (0,240,0),    # S — зелений
    (240,0,0)     # Z — червоний
]

# =============== 3. Код логіки гри ===================
# Кожна функція нижче робить маленьку, конкретну справу.


def create_new_piece():
    """Створює нову випадкову фігуру на старті зверху."""
    fig_idx = random.randrange(len(FIGURES))           # випадковий номер 0‑6
    shape   = [row[:] for row in FIGURES[fig_idx]]     # копія матриці форми
    x_start = FIELD_WIDTH // 2 - len(shape[0]) // 2    # центр по ширині
    y_start = 0                                        # верхній край
    return [shape, fig_idx, x_start, y_start]


def is_collision(piece, dx, dy):
    """Перевіряє: якщо зсунемо фігуру на (dx,dy) — вона вріжеться?"""
    shape, idx, px, py = piece
    for row_i, row in enumerate(shape):
        for col_i, cell in enumerate(row):
            if cell:                                   # розглядаємо лише блоки =1
                x = px + col_i + dx                    # нова горизонталь
                y = py + row_i + dy                    # нова вертикаль
                if x < 0 or x >= FIELD_WIDTH:          # вихід за лівий/правий край
                    return True
                if y >= FIELD_HEIGHT:                  # нижче дна
                    return True
                if y >= 0 and field[y][x]:             # в полі вже щось є
                    return True
    return False                                       # рух безпечний


def place_piece(piece):
    """Прикріплює фігуру до поля (робить її частиною декорацій)."""
    shape, idx, px, py = piece
    for r, row in enumerate(shape):
        for c, cell in enumerate(row):
            if cell:
                x = px + c
                y = py + r
                if 0 <= x < FIELD_WIDTH and 0 <= y < FIELD_HEIGHT:
                    field[y][x] = idx + 1              # +1 щоб 0 залишався «порожньо»


def clear_full_lines():
    """Видаляє повні рядки та додає зверху порожні — як у класичному Тетрісі."""
    global field
    field = [row for row in field if 0 in row]         # залишаємо рядки з хоча б одним 0
    while len(field) < FIELD_HEIGHT:                   # поки висота не 20
        field.insert(0, [0]*FIELD_WIDTH)               # додаємо порожній рядок угорі


def rotate_piece(piece):
    """Обертає фігуру на 90° (за годинниковою стрілкою)."""
    shape, idx, px, py = piece
    rotated = [list(col) for col in zip(*shape[::-1])]  # транспонуємо + перевертаємо
    return [rotated, idx, px, py]

# =============== 4. Ініціалізація Pygame ===============
pygame.init()
screen = pygame.display.set_mode((FIELD_WIDTH*CELL_SIZE,
                                   FIELD_HEIGHT*CELL_SIZE))
pygame.display.set_caption("Тетріс — навчальна версія")
clock = pygame.time.Clock()

current = create_new_piece()  # активна фігура
fall_timer = 0                # накопичує час, щоб знати коли опустити фігуру

game_over = False

# =============== 5. Головний цикл гри =================
while True:
    if game_over:
        pygame.time.wait(2000)
        break

    # ---- 5.1 Обробка подій клавіатури ----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and not is_collision(
                current, -1, 0):
                current[2] -= 1  # рух ліворуч
            elif event.key == pygame.K_RIGHT and not is_collision(
                current, 1, 0):
                current[2] += 1  # рух праворуч
            elif event.key == pygame.K_DOWN and not is_collision(
                current, 0, 1):
                current[3] += 1  # «швидке» падіння
            elif event.key == pygame.K_UP:
                rotated = rotate_piece(current)
                if not is_collision(rotated, 0, 0):
                    current = rotated

    # ---- 5.2 Таймер падіння ----
    fall_timer += clock.get_time()   # додаємо мс з попереднього кадру
    clock.tick(60)                  # тримаємо 60 FPS

    if fall_timer >= FALL_DELAY:
        if not is_collision(current, 0, 1):
            current[3] += 1  # опускаємо фігуру
        else:
            place_piece(current)    # закріплюємо
            clear_full_lines()      # перевіряємо на заповнені лінії
            current = create_new_piece()  # нова фігура
            if is_collision(current, 0, 0):
                game_over = True
        fall_timer = 0

    # ---- 5.3 Малювання ----
    screen.fill((20,20,20))  # фон − темно‑сірий

    # Малюємо всі «застиглі» блоки
    for y, row in enumerate(field):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(
                    screen,
                    COLORS[cell-1],
                    (x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
                )

    # Малюємо поточну рухому фігуру
    shape, idx, px, py = current
    for r, row in enumerate(shape):
        for c, cell in enumerate(row):
            if cell:
                pygame.draw.rect(
                    screen,
                    COLORS[idx],
                    ((px+c)*CELL_SIZE, (py+r)*CELL_SIZE, CELL_SIZE, CELL_SIZE)
                )

    pygame.display.flip()
