# Переводчик с гикского на русский
# Демонстрирует использование словарей
geek={"404":"Не знать, не владеть информацией. От сообщения об ошибке 404 'Страница не найдена'.",
      "Googling":"'Гугление', поиск в сети сведений о ком-либо.",
      "Keybofred Plague":"Мусор, который скапливается в клавиатуре компьютера.",
      "Link Rot":"Процесс устаревания гиперссылок на веб-страницах.",
      "Percussive Maintenance":"О ситуации, когда кто-либо бьет по корпусу неисправного электронного прибора в надежде восстановить его работу",
      "Uninstalled":"Об увольнении кого-либо. Особенно популярно на рубеже 1990-2000-х годов."}
choice=None
while choice!="0":
    print(
        """
        Переводчик с гикского на русский
        0 - Выйти
        1 - Найти толкование термина
        2 - Добавить термин
        3 - Изменить толкование
        4 - Удалить термин
        """
        )
    choice=input("Ваш выбор: ")
    print()
    # выход
    if choice =="0":
        print("До свидания.")
    # поиск толкования
    elif choice=="1":
        term=input("Какой термин вы хотите перевести с гикского на русский? ")
        if term in geek:
            definition=geek[term]
            print("\n",term,"оначает",definition)
        else:
            print("\nУвы, этот термин мне не знаком: ",term)
    # добавление термина с толкованием
    elif choice=="2":
        term=input("Какой термин гикского языка вы хотите добавить? ")
        if term not in geek:
            definition=input("\nВпишите ваше толкование: ")
            geek[term]=definition
            print("\nТермин",term,"добавлен в словарь.")
        else:
            print("\nТакой термин уже есть! Попробуйте изменить его толкование.")
    # новое токование известного темина
    elif choice=="3":
        term=input("Какой термин вы хотите переопределить? ")
        if term in geek:
            definition=input("Впишите ваше толкование: ")
            geek[term]=definition
            print("\nТермин",term,"переопределен.")
        else:
            print("\nТакого термина пока нет! Попробуйте добавить его в словарь.")
    # удаление термина вместе с его толкованием        
    elif choice=="4":
        term=input("Какой термин вы хотите удалить? ")
        if term in geek:
            del geek[term]
            print("\nТермин",term,"удален.")
        else:
            print("\nНичем не могу помочь. Термина",term,"нет в словаре.")
    # непонятный пользовательский ввод
    else:
        print("Извините, в меню нет пункта",choice)
input("\n\nНажмите Enter, чтобы выйти.")        
