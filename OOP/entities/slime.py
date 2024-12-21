import pygame
from settings import slime_size, SPEED, ANIMATTION_SPEED
from settings import SLIME_IMAGE_PATH, WIDTH, HEIGHT
from entities.entity import Entity
import math

class Slime(Entity):
    def __init__(self,x,y):
        # Виклик конструктору базового класу
        super().__init__(SLIME_IMAGE_PATH, slime_size)
        self.rect.center = (x,y) # Початкова позиція слайма
        self.direction = 0 # Кут руху у градусах
        self.moving = False # Чи рухається (індикатор стану)
        self.current_scale_x = 1.0 # Поточний масштаб по X
        self.current_scale_y = 1.0 # Поточний масштаб по Y
        self.velocity = pygame.math.Vector2(0,0) # Вектор руху

    # Функція для обробки руху слайма
    def move(self, keys):
        self.velocity.update(0,0) # Скидання вектора швидкості
        self.moving = False # Початково вважається, що напрямку 
                            # немає
        # Перевірка натиснутих клавіш
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.velocity.y = -1 # Рух вгору
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.velocity.y = 1 # Рух вниз
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.velocity.x = -1 # Рух ліворуч
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.velocity.x = 1 # Рух праворуч

        # Якщо вектор швидкості не нульовий
        if self.velocity.length_squared() > 0:
            # Нормалізація та застосування швидкості
            self.velocity = self.velocity.normalize() * SPEED
            self.moving = True # Встановлення прапора руху
            # Визначення кута напрямку руху
            self.direction = math.degrees(math.atan2(
                -self.velocity.y, self.velocity.x)) % 360
        
        # Оновлення позиції персонажа
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y
        # Обмеження руху в межах екрану
        self.rect.clamp_ip(pygame.Rect(0,0, WIDTH, HEIGHT))
    
    def lerp(self, a, b, t):
        """ Лінійна інтероляція між "a" та "b" з коефіцієнт "t". """
        return a + (b - a) * t