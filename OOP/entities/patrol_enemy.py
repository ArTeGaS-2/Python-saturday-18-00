import pygame
import math
from entities.enemy import Enemy
from settings import (VERTICAL_ENEMY_SPEED,
                      ENEMY_IMAGE_PATH, ENEMY_SIZE)

class PatrolEnemy(Enemy):
    """
    Ворог, що патрулює між списком точок,
    перемикаючись до наступної, коли досягає поточної.
    """
    def __init__(self, patrol_points):
        super().__init__(ENEMY_IMAGE_PATH, ENEMY_SIZE)

        self.speed = VERTICAL_ENEMY_SPEED
        self.patrol_points = patrol_points
        self.current_index = 0

        # Ставимо першу точку
        if self.patrol_points:
            self.rect.center = self.patrol_points[self.current_index]
    
    def update(self, *args):
        # Якщо немає точок - нічого не робимо
        if not self.patrol_points:
            return
        # Цільова точка
        target = self.patrol_points[self.current_index]
        dx = target[0] - self.rect.centerx
        dy = target[1] - self.rect.centery

        distance = math.hypot(dx, dy)
        if distance < 1: # Якщо дійшли до точки - переключаємось
            self.current_index = (self.current_index + 1
                                  ) % len(self.patrol_points)
        else: # Рухаємось у напрямку точки
            dx_norm = dx / distance
            dy_norm = dy / distance
            self.rect.x += dx_norm * self.speed
            self.rect.y += dy_norm * self.speed

    def handle_collision_with_player(self, player):
        pass
