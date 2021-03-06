# Случайные буквы
# Демонстрирует индексацию строк

## глава 4 учебника Доусона

import random

# переменная имеет строковое значение, где "и" стоит в позиции 0 (ноль)
## >>> word="индекс"
## >>> print(word[0])
## и
## >>> print(word[1])
## н
## обычная последовательность начинается с нуля(0), отрицательная с (-1)

word="индекс"
print("В переменной word хранится слово: ",word,"\n")

# в переменной high будет число 6, т.к. в слове "индекс" 6 букв

high=len(word)

# переменной low будет -6
# таким образом команда position будет иметь диапазон от -6,..0,.. до 5

low=-len(word)

# цикл range произведет операцию 10 раз

for i in range(10):
# выбирается случайная позиция, программа выводит номер и символ этой позиции    
    position=random.randrange(low,high)
    print("word[",position,"]\t",word[position])
input("\nНажмите Enter, чтобы выйти.")    
