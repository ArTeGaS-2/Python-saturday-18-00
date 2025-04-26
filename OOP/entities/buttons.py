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
    
class PauseButton(Button):
    """ Кнопка  "Пауза": змінює self.game_manager.paused """
    def __init__(self, image_path, pos, game_manager):
        super().__init__(image_path, pos)
        self.game_manager = game_manager

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
        # Отримуємо позицію курсора і перевіряємо чи клік у межах Rect:
            if self.rect.collidepoint(event.pos):
                # Перемикаємо паузу
                self.game_manager.paused = not self.game_manager.paused
    
# ----/----/----/----/----/----/----/----/

class ExitButton(Button):
    def __init__(self, image_path, pos):
        super().__init__(image_path, pos)
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                pygame.quit()
                exit()
    
