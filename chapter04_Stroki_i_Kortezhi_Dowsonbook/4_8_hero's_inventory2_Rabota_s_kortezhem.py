# Арсенал героя 2.0
# Демострирукет работу с кортежами

# глава 4 учебника Доусона

# создадим кортеж с несколькими элементами и выведем его с помощью цикла for
inventory=("меч",
           "кольчуга",
           "щит",
           "целебное снадобье")
print("\nИтак, в вашем арсенале:")
for item in inventory:
    print(item)
input("\nнажмите Enter, чтобы продолжить.")
# найдем длину кортежа
print("Сейчас в вашем распоряжении",len(inventory)," предмета/-ов.")
input("\nнажмите Enter, чтобы продолжить.")
# проверка на принадлежность кортежу с помощью in
if "целебное снадобье" in inventory:
    print("Вы ещё поживете и повоюете.")
# вывод одного элемента с определенным индексом
index=int(input("\nВведите индекс одного из предметов арсенала: "))
print("Под индексом",index,"в арсенале находится",inventory[index])
# отобразим срез
start=int(input("\nВведите начальный индекс среза: "))
finish=int(input("Введите конечный индекс среза: "))
print("Срез inventory[",start,":",finish,"]-это",end=" ")
print(inventory[start:finish])
input("\nнажмите Enter, чтобы продолжить.")
# соединим два кортежа
chest=("золото","драгоценные камни")
print("Вы нашли ларец. Вот, что в нем есть:")
print(chest)
print("Вы приобщили содержимое ларца к своему арсеналу.")
# цепление 2-х кортежей, содержимое их не меняется
inventory+=chest
print("Теперь в вашем арсенале:")
print(inventory)
input("\nНажмите Enter, чтобы выйти.")