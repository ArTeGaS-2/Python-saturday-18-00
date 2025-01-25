import pygame
import random
from entities.enemy import Enemy
from settings import( WIDTH, HEIGHT, ENEMY_IMAGE_PATH,
    ENEMY_SIZE, VERTICAL_ENEMY_SPEED)

class VerticalEnemy(Enemy):
    """
    Ворог, що рухається зверху екрану вниз.
    Якщо виходить за межі - знову з'являється зверху
    """
    def __init__(self):
        super().__init__(ENEMY_IMAGE_PATH, ENEMY_SIZE)
        self.speed = VERTICAL_ENEMY_SPEED
        # Початкова позиція: випадковий X, за верхнім краєм
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = -self.rect.height

    def update(self, *args):
        # Рух вниз
        self.rect.y += self.speed
        # Якщо пішли за екран - повертаємо нагору
        if self.rect.top > HEIGHT:
            self.rect.bottom = 0
            self.rect.x = random.randint(0, WIDTH - self.rect.width)
    
    def handle_collision_with_player(self, player):
        # Поки немає обробки колізій
        pass