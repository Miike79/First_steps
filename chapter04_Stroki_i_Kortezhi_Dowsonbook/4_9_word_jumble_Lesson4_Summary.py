# Анаграммы
#
# Компьютер выбирает какое-либо слово и хаотически перставляет буквы
# Задача игрока восстановить исходное слово

# глава 4 учебника Доусона

import random
# создадим последовательность слов(константу), из которых прога выбирает
WORDS=("питон","анаграмма","простая","сложная","ответ","подстаканник")
# случайным образом выберем из последовательности одно слово
word=random.choice(WORDS)
# создадим переменную, с которой будет затем составлена версия игрока
correct=word
# создадим анаграмму выбранного слова, в которой буквы будут расставлены
# хаотично
jumble=""
# цикл while будет выполнятся, пока в строке word не останется значений
while word:
    # выбирается случайная позиция из значений в строке word
    position=random.randrange(len(word))
    # создается новая строка из этой позиции, к ней + следующие позиции
    jumble+=word[position]
    # от word отделяются значения, пока оно не станет пустым
    word=word[:position]+word[(position+1):]
#начало игры
print(
    """
            Добро пожаловать в игру 'Анаграммы'!
        Надо переставить буквы так, чтобы получилось осмысленное слово.
     (Для выхода нажмите Enter, не вводя своей версии.)
     """
    )
print("Вот анаграмма:",jumble)
guess=input("\nПопробуйте отгадать исходное слово: ")
while guess != correct and guess !="":
    print("К сожалению, вы не правы.")
    guess=input("Попробуйте отгадать исходное слово: ")
if guess == correct:
    print("Да! Именно так! Вы отгадали!\n")
print("Спасибо за игру!")
input("\nНажмите Enter, чтобы выйти.")
