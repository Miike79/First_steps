# Резчик пиццы
# Демонстрирует срезы строк

## глава 4 учебника Доусона

word="пицца"
print(
    """
Памятка
0   1   2   3   4   5
+---+---+---+---+---+
I п I и I ц I ц I а I
+---+---+---+---+---+
-5  -4  -3  -2  -1
"""
    )
print("Введите начальный и конечный индексы для того среза 'пиццы', который"+
      " хотите получить.")
print("Для выхода нажмите Enter, не вводя начальную позицию.")
# значение None - пустое значение, ещё не присвоенное, рассматривается как False
start=None
while start !="":
    start=(input("\nНачальная позиция: "))
    if start:
        start=int(start)
        finish=int(input("Конечная позиция: "))
        print("Срез word[",start,":",finish,"]выглядит как",end=" ")
        print(word[start:finish])
input("\nНажмите Enter, чтобы выйти.")        
    
