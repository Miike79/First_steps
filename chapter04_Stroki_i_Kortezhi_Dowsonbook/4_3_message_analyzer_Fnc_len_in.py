# Анализатор текста
# Демонстрирует работу функции len() и оператора in
 
## глава 4 учебника Доусона

message=input("Введите текст: ")

# функция len считает длину последовательности - все элемнты в ней, вкл. пробелы

print("\nДлина введенного вами текста составляет:",len(message))
print("\nСамая частая согласная,'т',")

# в строке переменной (message) ищется символ ("т")
# оператор in узнает является ли членом последовательности искомый элемент
## символ "Т" заглавная здесь не будет учтен как "т"

if "т" in message:
    print("встречается в вашем тексте.")
else:
    print("не встречается в вашем тексте.")
input("\nНажмите Enter, чтобы выйти.")    
