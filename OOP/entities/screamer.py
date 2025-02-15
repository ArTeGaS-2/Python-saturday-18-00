import pygame

class Screamer:
    def __init__(self):
        # Початкове значення: не активний
        self.active = False

        # Завантажуємо зображення
        self.image = pygame.image.load(
            "OOP/assets/screamer.png").convert_alpha()
        # Завантажуємо звук
        self.sound = pygame.mixer.Sound("OOP/assets/screamer.mp3")
        self.sound.set_volume(0.5) # Гучність від 0 до 1

    def resize(self, width, height):
        """Масштабуємо зображення під розмір екрану"""
        self.image = pygame.transform.scale(
            self.image, (width, height))
    def activate(self):
        """Активуємо скрімер"""
        if not self.active:
            self.active = True
            if self.sound:
                self.sound.play(loops = 0, maxtime = 2000)
    def deactivate(self):
        """Деактивуємо скрімер"""
        if self.active:
            self.active = False
            if self.sound:
                #self.sound.stop()
                pass
    def draw(self, screen):
        """Малюємо скрімер на екрані, якщо він активний"""
        if self.active and self.image:
            screen.blit(self.image, (0, 0))
    
        
    