import random # файл з бібліотекою(функціонлом) випадкових чисел

number = random.randint(0,100) # випадкове число від 0 до 100
print("Вгадай число від 1 до 100:")
while True:
    guess = int(input("Твій варіант:")) # Введення гравцем
    if guess < number: # Якщо ти ввів меньше
        print("Більше...")
    elif guess > number: # Якщо ти ввів більше
        print("Меньше...")
    elif guess == number: # Якщо вгадав загадане число
        print("Вітаю! Число:" + str(number))
        break # Зупиняє гру
