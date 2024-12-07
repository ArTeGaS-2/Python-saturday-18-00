class Conspect:
    # Класс об'єкту - контейнер для методів і змінних
    # що уособлюють собою певний абстрактний або реальний
    # об'єкт
    def __init__(self):
        # Метод __init__ - конструктор классу. Є на початку
        # кожного класу. Потрібен для побудови екземплярів
        self.a = 2 # Ціле число
        self.b = 4.3 # Дробове число
        self.logic = True # Логічна змінна (True/False)
        self.tempList = [3,6,4,4] # Список
        
    def Operators(self):
        # Математичні оператори
        c = self.a + self.b # Додавання
        c = self.a - self.b # Віднімання
        c = self.a * self.b # Множення
        c = self.a / self.b # Ділення

        # Порівняльні та логічні оператори
        if self.a > self.b: pass # a більше за b
        if self.a < self.b: pass # a меньше за b
        if self.a >= self.b: pass # a більше або дорівнює b
        if self.a <= self.b: pass # a меньше або дорівнює b
        if self.a == self.b: pass # Порівнюємо чи дорівнюють
        if self.a != self.b: pass # Перевіряємо щоб не дорівнювало

        # Логічний оператор "and" перевіряє виконання кожної
        # з умов (2 або більше)
        if self.a == self.b and self.logic: pass

        # Логічний оператор "or" перевіряє виконання хоча б
        # однієї з умов
        if self.a == self.b or self.logic: pass