# Зверюшка с атрибутами
# Демонстрирует создание атрибутов обьекта и доступ к ним

# глава 8 учебника Доусона
class Critter(object):
    """Виртуальный питомец"""

    def __init__(self, name):
        print("Появилась на свет новая зверюшка!")
        self.name = name

    # метод, который выводит объект на экран с помощью строк
    def __str__(self):
        rep = "Обьект класса Critter\n"
        rep += "имя: " + self.name + "\n"
        return rep

    def talk(self):
        print("Привет. Меня зовут", self.name, "\n")


# основная часть
# создавая переменную crit мы инициализируем объект класса Critter
# и вносим туда переменную name, которая формирует атрибут "Бобик" у объекта
crit1 = Critter("Бобик")
# вызываем метод talk у объекта crit
# т.к. в методе talk есть ссылка на объект self, а объект self инициирован с
# атрибутом name, а name мы прописали "Бобик"
crit1.talk()
crit2 = Critter("Мурзик")
crit2.talk()
print("Вывод объекта crit1 на экран:")
print(crit1)
print("Непосредственный доступ к атрибуту crit1.name:")
# сейчас осуществим прямой доступ кода к атрибуту вне его класса
print(crit1.name)
input("\nНажмите Enter, чтобы выйти")
