# Симулятор трехлетнего ребенка
# Демонстрирует работу цикла while

# глава 3 учебника Доусона

print("Добро пожаловать в программу 'Симулятор трехлетнего ребенка'\n")
print("Имитируется разговор с маленьким ребенком.")
print("Попробуйте остановить этот кошмар.\n")
response = ""
while response != "потому что":
    response = input("Почему?\n")
print('А, ладно.')
input("\nНажмите Enter, чтобы выйти.")
