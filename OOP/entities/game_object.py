from settings import OBJECT_IMAGE_PATH, object_size, WIDTH, HEIGHT
from entities.entity import Entity
import random

class GameObject(Entity):
    def __init__(self):
        super().__init__(OBJECT_IMAGE_PATH, object_size)
        self.rect.topleft = self.spawn()

    def spawn(self):
        x = random.randint(0, WIDTH - self.rect.width)
        y = random.randint(0, HEIGHT - self.rect.height)
        return (x,y)