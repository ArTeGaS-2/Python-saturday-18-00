# 1.Створіть клас Character, який матиме такі атрибути
# - name(текстовий тип)
# - level(цілий тип)
# - health(дробовий тип)

# 2. Створіть конструктор __init__, що прийматиме значення цих
# атрибутів

# 3. Створіть 3-5 об'єктів класу Character з різними початковими
# даними та додайте їх до списку characters.

# 4.Виведіть інформацію про кожного персонажа в консоль
# Інструменти: списки, цикл for, базові типи даних

class Character:
    def __init__(self, name, level, health):
        self.name = name
        self.level = level
        self.health = health

knight = Character("Artur", 3, 50)
archer = Character("Orlando Blum", 4, 30)
mage = Character("Gendalf", 5, 15)

chars = [knight, archer, mage]

for char in chars:
    print(f"Name:{char.name}, Level:{char.level}, Health: {char.health}")
    