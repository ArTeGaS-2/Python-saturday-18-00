import pygame

class Button:
    """Базова кнопка: завантажує зображення, малює перевіряє клік"""
    def __init__(self, image_path, pos):
        # Завантажуємо зображення
        self.image = pygame.image.load(image_path).convert_alpha()
        # Робимо Rect для відстеження зіткнень
        self.rect = self.image.get_rect()
        # Розташовуємо кнопки
        self.rect.topleft = pos

    def draw(self, screen):
        """Малюємо кнопку на екрані"""
        screen.blit(self.image, self.rect)

    def handle_event(self, event):
        """Обробка подій"""
        pass
# ----/----/----/----/----/----/----/----/
    
