import pygame
from game_manager import GameManager

def show_menu():
    pygame.init() # Ініціалізація Pygame
    screen = pygame.display.set_mode((800,600)) # Розмір вікна меню
    pygame.display.set_caption("Головне меню")

    # Завантажуємо зображення кнопок
    start_img = pygame.image.load("OOP/assets/start_button.png").convert_alpha()
    exit_img = pygame.image.load("OOP/assets/exit_button.png").convert_alpha()

    start_img = pygame.transform.scale(start_img,(256,128))
    exit_img = pygame.transform.scale(exit_img,(256,128))

    # Створюємо прямокутники (rect)
    start_rect = start_img.get_rect(center=(400, 250)) # Позиція кнопки Старт
    exit_rect = exit_img.get_rect(center=(400,350))    # Позиція кнопки Вихід

    # Цикл головного меню
    while True:
        # Обробка подій
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Отримуємо координати кліку
                mouse_pos = pygame.mouse.get_pos()
                # Перевіряємо, чи клікнув користувач по кнопці "Старт"
                if start_rect.collidepoint(mouse_pos):
                    return
                # Перевіряємо, чи клікнув користувач по кнопці "Вихід"
                if exit_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    exit()
        # Заливаємо фон
        screen.fill((200,220,255))
        # Малюємо кнопки
        screen.blit(start_img,start_rect)
        screen.blit(exit_img,exit_rect)
        # Оновлюємо вікно
        pygame.display.flip()
def main():
    show_menu()

    game = GameManager()
    game.run()

if __name__ == "__main__":
    main()