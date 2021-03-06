# Классово верная зверюшка
# Демонстрирует атрибуты класса и статические методы

# глава 8 учебника Доусона
class Critter(object):
    """Виртуальный питомец"""
    # это атрибут класса, создает каждая команда внутри класса,
    # но вне любого из его методов
    # атрибут класса появляется прежде, чем появляется хотя бы один объект
    # этим атрибутом можно пользоваться даже пока нет объектов
    total = 0

    # через декоратор @ объявляется СТАТИЧЕСКИЙ метод, после этого метод
    # будет применятся к классу, не к объекту, поэтому вместо ссылки (self) будет ()
    @staticmethod
    def status():
        print("\nВсего зверюшек сейчас", Critter.total)

    def __init__(self, name):
        print("Появилась на свет новая зверюшка!")
        self.name = name
        # добавляет к атрибуту класса Critter +1 при иниц. каждого нового объекта
        Critter.total += 1


# основная часть
Critter.status()
print("Нахожу значение атрибута класса Critter.total: ", end="")
# пока не иниц ни одной зверюшки, значение total класса Critter=0
print(Critter.total)
print("\nСоздаю зверюшек.")
# после инициации каждого объекта прибавляется значение total в классе
crit1 = Critter("Зверюшка 1")
crit2 = Critter("Зверюшка 2")
crit3 = Critter("Зверюшка 3")
# вызов СТАТИЧЕСКОГО метода класса, без ссылки на объект
Critter.status()
print("\nОбращаюсь к атрибуту класса через объект: ", end="")
# через объект класса crit1 (можно через любой объект и crit2 и crit3)
# можно получить доступ к атрибуту класса total, не явл. атрибутом объектов
print(crit1.total)
input("\nНажмите Enter, чтобы выйти")
