import pygame
from settings import(WIDTH, HEIGHT, background_color, spawn_interval, FPS)
from entities.slime import Slime
from entities.game_object import GameObject

# Імпортуємо класи ворогів
from entities.vertical_enemy import VerticalEnemy
from entities.patrol_enemy import PatrolEnemy
from entities.crow_enemy import CrowEnemy 

# Скрімер
from entities.screamer import Screamer

import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

from entities.buttons import PauseButton, ExitButton

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

        # Створюємо глобальний скрімер
        self.screamer = Screamer()
        self.screamer.resize(WIDTH,HEIGHT)

        # Група ворогів
        self.enemies = pygame.sprite.Group()

        # Створення слайма
        self.slime = Slime(WIDTH // 2, HEIGHT // 2) # Екземпляр классу Slime
        self.all_sprites.add(self.slime)

        # Створюємо ворогів і додаємо їх у групи
        vertical_enemy = VerticalEnemy()
        self.all_sprites.add(vertical_enemy)
        self.enemies.add(vertical_enemy)

        patrol_points = [ # Список точок маршруту
            (100, 100), # x та y для першої
            (WIDTH - 100, 100),
            (WIDTH - 100, HEIGHT - 100),
            (100, HEIGHT - 100)]
        patrol_enemy = PatrolEnemy(patrol_points)

        self.all_sprites.add(patrol_enemy)
        self.enemies.add(patrol_enemy)

        crow_enemy = CrowEnemy(self.slime)
        self.all_sprites.add(crow_enemy)
        self.enemies.add(crow_enemy)

        # Час від останнього спавну
        self.last_spawn_time = pygame.time.get_ticks() 
        self.collected_objects = 0 # Кількість зібраних об'єктів

        # Стан паузи
        self.paused = False

        # Створюємо кнопки
        self.pause_button = PauseButton(
            "OOP/assets/ingame_pause_button.png",
            (WIDTH - 240, 10), self)
        self.exit_button = ExitButton(
            "OOP/assets/ingame_exit_button.png",
            (WIDTH - 120, 10))

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

            self.pause_button.handle_event(event)
            self.exit_button.handle_event(event)

    def update(self):
        if self.paused:
            return

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

        # Перевірка зіткнень з ворогами
        collision_found = False
        for enemy in self.enemies:
            if pygame.sprite.collide_rect(self.slime, enemy):
                enemy.handle_collision_with_player(self.slime)
                collision_found = True

        if collision_found: self.screamer.activate()
        else: self.screamer.deactivate()

    def draw(self):
        self.screen.fill(self.background_color)
        self.all_sprites.draw(self.screen)
        self.display_score()
        self.screamer.draw(self.screen)

        self.pause_button.draw(self.screen)
        self.exit_button.draw(self.screen)

    def display_score(self):
        text = self.font.render(f'Зібрано: {self.collected_objects}',
                                 True, (0,0,0))
        self.screen.blit(text, (10,10))