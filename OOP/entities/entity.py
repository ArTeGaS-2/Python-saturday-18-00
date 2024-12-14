import pygame

# Класс - контейнер для абстракції
class Entity(pygame.sprite.Sprite): # Класс Entity наслідує Sprite(базовий у pygame)
    def __init__(self, image_path, size): # Приймає аргументи image_path і size
        super().__init__() # Наслідує конструктор класу Sprite

        # Завантаження зображення
        self.original_image = pygame.image.load(image_path).convert_alpha()
        # Зміна розміру
        self.image = pygame.transform.scale(self.original_image, size)
        # Отримуємо прямокутник зображення
        self.rect = self.image.get_rect()