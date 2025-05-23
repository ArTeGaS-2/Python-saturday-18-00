class Character:
    def __init__(self, name, level, health):
        self.name = name
        self.level = level
        self.health = health
    
    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            print(f"{self.name} вибуває з гри.")
        else:
            print(f"{self.name} отримав {amount} ушкоджень. Залишилось: {self.health}")
            

knight = Character("Artur", 3, 50)

knight.take_damage(24)

damage = 40
if damage > 0:
    knight.take_damage(damage)
else:
    print("Немає пошкоджень.")



