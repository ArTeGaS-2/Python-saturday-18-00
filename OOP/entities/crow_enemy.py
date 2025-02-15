import pygame
import math
import random
from entities.enemy import Enemy
from settings import(WIDTH, HEIGHT, ENEMY_IMAGE_PATH,
                     ENEMY_SIZE, VERTICAL_ENEMY_SPEED)

class CrowEnemy(Enemy):
    """
    Ворог(прототип - ворон) що летить в бік гравця, переслідуючи
    """
    def __init__(self, player):
        super().__init__(ENEMY_IMAGE_PATH,ENEMY_SIZE)
        self.speed = VERTICAL_ENEMY_SPEED
        self.player = player # Змінна для пошуку гравця

        # Початкова позиція
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = -self.rect.height

        self.base_image = self.image

    def update(self, *args):
        # Отримуємо позицію гравця
        px,py = self.player.rect.center
        dx = px - self.rect.centerx
        dy = py - self.rect.centery

        distance = math.hypot(dx,dy)

        if distance != 0:
            dx_norm = dx / distance
            dy_norm = dy / distance
            self.rect.x += dx_norm * self.speed
            self.rect.y += dy_norm * self.speed

    def handle_collision_with_player(self, player):
        pass