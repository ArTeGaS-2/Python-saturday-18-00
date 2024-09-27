import random # Імпортуємо модуль для випадкових чисел

def play_game():

    attempts = 0 # Спроби
    max_attempts = 5 # Максимальна кількість спроб

    # Загадуємо число від 1 до 100
    secret_number = random.randint(1,100)

    # print(secret_number)

    guess = None

    # Перевіряє чи виконунуються умови (загадане не дорівнює вписаному)
    # або (кількість спроб не більше за максимальну кількість спроб)
    while guess != secret_number and attempts < max_attempts:
        try:
            # Отримуємо число від гравця
            guess = int(input("Введіть число від 1 до 100: \n"))

            # Додає до лічильника спроб 1 при неправильній відповіді
            attempts += 1

            # Виконується, якщо введене число меньше за загадане
            if guess < secret_number:
                print("Загадане число більше!")

            # Виконується, якщо введене число більше за загадане
            elif guess > secret_number:
                print("Загадане число меньше!")
            # Виконується, якщо жодна з умов не вірна
            else:
                print(f"Вітаю, ви вгадали число за {attempts} спроб!")
        except ValueError:
            print("будь ласка, введіть ціле число!")

    # Виконується, якщо вичерпано максимальну кількість спроб і число не вгадано
    if attempts == max_attempts and guess != secret_number:
        print(f"Ви не вгадали! Загадане число {secret_number}")

def choose_difficulty():
    print("Виберіть рівень складності:")
    print("1. Легкий (1-10, 5 спроб)")
    print("2. Середній (1-50, 7 спроб)")
    print("3. Складний (1-100, 10 спроб)")
    choise = input("Ваш вибір (1/2/3):")
    if choise == '1':
        return 1, 10, 5
    elif choise == '2':
        return 1, 50, 7
    elif choise == '3':
        return 1, 100, 10

play_again = 'так'

while play_again.lower() == 'так':
    play_game()
    play_again = input("Бажаєте зіграти ще раз? (так/ні) \n")