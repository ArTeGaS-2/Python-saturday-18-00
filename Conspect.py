# Основні типи даних
age = 25 # int
height = 1.75 # float
name = "Ібрагім" # string або str
is_human = True # bool або boolean

# Основні типи колекцій даних
fruits = [] # Пустий список (list)

# Наповнений список
full_of_fruits = ["Груша", "Банан",
                   "Яблуко", "Персик"]

full_of_fruits.append("Фейхуа")

names = () # Пустий кортеж

# Наповнений кортеж
full_of_names = ("Ілля", "Антоніна", "Фіїна")

#full_of_names.append("Іван")

ages = {} # Пустий словник

# Наповнений словник
full_of_ages = {'Богдан': 12,
                "Леонід":58,
                "Анастасія":16}

# Цикли

# Цикл for для перебору списку
for fruit in full_of_fruits:
    print(fruit)

# Цикл while працює допоки дійсна умова
counter = 0
finish_count = 10000
while counter < finish_count:
    counter += 1
    print(counter)

# Умовні оператори
if counter < 5:
    print("") # Якщо умова вірна
elif counter < 6:
    print("") # Якщо не вірна умова if, але вірна ця
else: 
    print("") # Якщо не вірна жодна з умов

#Потрібно використати список, цикл, print

#Інгредієнти піци:
#Тісто
#Томат
#Ковбаса
#Сир

#Умовні оператори

#Перевірити чи присутнє чілі
