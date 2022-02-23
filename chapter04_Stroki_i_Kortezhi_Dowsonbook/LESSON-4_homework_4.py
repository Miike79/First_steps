# Угадай слово

# игрок должен отгадать слово
# компьютер сообщает сколько букв в слове и дает 5 попыток, есть ли буква
# программа отвечает только да или нет

import random

# создадим последовательность слов(константу), из которых прога выбирает
WORDS = ("кошка", "собака", "корова", "лошадь", "коза", "баран")
# случайным образом выберем из последовательности одно слово
word = random.choice(WORDS)
# создадим переменную, с которой будет затем составлена версия игрока
correct = word
tries = 1
# объяснение правил
print(
    """
                 Добро пожаловать в игру 'Угадай слово'!
    Программа загадает домашнее животное, которое вам предстоит отгадать.
        Вам будет известно количество букв и дано 5 попыток угадать,
                  какие буквы есть в слове. Начали...
    """
)
# прописываем подсказку из скольких букв состоит слово
print("Загаданное слово состоит из ", len(word), " букв.\n")
# задаем переменную букву
char = input("Какая буква может быть в слове? : ")
if char in word:
    print("Буква '", char, "' есть в слове!")
else:
    print("Буквы '", char, "' нет в слове!")
# задаем условие при котором игрок может написать слово или запрсить подсказку.
slovo = input("Отгадайте слово и нажмите Enter (или просто нажмите Enter, если вам нужно больше букв): ")
# устанавливаем цикл или до верного слова или до 5 попыток
while slovo.lower() != correct and tries <= 5:
    if slovo.lower() != correct and slovo.lower() != "":
        print("Не угадали! Попробуйте ещё раз!")
    char = input("\nКакая буква может быть в слове? : ")
    if char in word:
        print("Буква '", char, "' есть в слове!")
    else:
        print("Буквы '", char, "' нет в слове!")
    slovo = input("Отгадайте слово и нажмите Enter (или просто нажмите Enter, если вам нужно больше букв): ")
    tries += 1
# задаем условие, какое сообщение появляется в зависимости от результата
if tries <= 5:
    print("Да! Именно так! Вы отгадали слово \"", word, "\" ! Потрачено попыток - ", tries, "\n")
else:
    print("К сожалению, вам не удалось отгадать слово.")
print("Спасибо за игру!")
input("\nНажмите Enter, чтобы выйти.")