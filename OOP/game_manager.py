import pygame
from settings import(WIDTH, HEIGHT, background_color, spawn_interval, FPS)
from entities.slime import Slime
from entities.game_object import GameObject

class GameManager:
    def __init__(self):
        pygame.init() # Ініціалізація pygame
        # Ширина та висота ігрового поля/ екрану
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        # Заголовок вікна
        pygame.display.set_caption("Їстівна планета")
        # Ігровий час та FPS 
        self.clock = pygame.time.Clock()
        # Фон та шрифт
        self.background_color = pygame.Color(background_color)
        self.font = pygame.font.SysFont(None, 36)

        # Створення спрайт-груп
        self.all_sprites = pygame.sprite.Group()
        self.collectibles = pygame.sprite.Group()

        # Створення слайма
        self.slime = Slime(WIDTH // 2, HEIGHT // 2) # Екземпляр классу Slime
        self.all_sprites.add(self.slime)

        # Час від останнього спавну
        self.last_spawn_time = pygame.time.get_ticks() 
        self.collected_objects = 0 # Кількість зібраних об'єктів

    def run(self):
        running = True
        while running:
            self.clock.tick(FPS) # Встановлюємо кадри на секунду
            self.handle_events() # Основний обробник подій
            self.update() # Трекінг подій у грі і натискань клавіш
            self.draw() # Відмальовування всіх зображень
            pygame.display.flip()
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get(): # Основний обробник
            if event.type == pygame.QUIT: # Обробка закриття вікна
                pygame.quit()
                exit()

    def update(self):
        keys = pygame.key.get_pressed() # Список клавіш 
        self.all_sprites.update(keys) # Оновлення положення об'єктів

        # Спавн об'єктів з інтервалом
        current_time = pygame.time.get_ticks() # Поточний час від точки відліку
        # Якщо "поточний час" - "час останного спавну" більше за інтервал
        if (current_time - self.last_spawn_time) >= spawn_interval * 1000:
            obj = GameObject() # Екземпляр класу GameObject
            self.all_sprites.add(obj) 
            self.collectibles.add(obj)
            self.last_spawn_time = current_time # Оновлення часу останнього спавну
        
        # Перевірка на зіткнення
        collided = pygame.sprite.spritecollide(
            self.slime, self.collectibles, True) 
        self.collected_objects += len(collided)

    def draw(self):
        self.screen.fill(self.background_color)
        self.all_sprites.draw(self.screen)
        self.display_score()

    def display_score(self):
        text = self.font.render(f'Зібрано: {self.collected_objects}',
                                 True, (0,0,0))
        self.screen.blit(text, (10,10))