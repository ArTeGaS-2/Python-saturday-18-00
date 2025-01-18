import pygame
from entities.entity import Entity

class Enemy(Entity):
    """
    Базовий абстрактний класс ворога.
    """
    def __init__(self, image_path, size):
        super().__init__(image_path, size)

    def update(self, *args):
        """
        Метод оновлення ворога.
        """
        pass
    
    def handle_collision_with_player(self, player):
        pass