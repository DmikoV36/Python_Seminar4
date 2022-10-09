# Сделать локальный чат-бот с JSON хранилищем на основе приложенного буткемпа. Тема чат-бота любая. Просьба - постараться не использовать простой одномерный список.

import json
all_info = []
wishes = ""

def load():
    global all_info
    with open ("BD.json", "r", encoding = "utf-8") as bd:
        all_info = json.load(bd)
    print("Актуальная информация по фитнес-центру была успешно загружена")

def save():
    with open("wish.json", "a", encoding = "utf-8") as wi:
        wi.write(json.dumps(wishes, ensure_ascii = False))
    print ("Ваше обращение будет рассмотрено в ближайщее время. Администратор клуба позвонит Вам!")

while True:
    command = input("Введите команду: ")
    if command == "/start":
        print("Добро пожаловать в чат-бот нашего фитнес-центра!")
        load()
    elif command == "/stop":
        print("Бот остановил свою работу. Будем рады видеть Вам снова!")
        break
    elif command == "/events":
        print("Список всех мероприятий центра:")
        print(all_info[0])
    elif command == "/instructor":
        print("Список тренерского состава:")
        print(all_info[1])
    elif command == "/schedule1":
        print("Расписание тренажерного зала:")
        print(all_info[2][0])
    elif command == "/schedule2":
        print("Расписание занятий по йоге:")
        print(all_info[2][1])
    elif command == "/schedule3":
        print("Расписание занятий по танцам:")
        print(all_info[2][2])
    elif command == "/schedule4":
        print("Расписание массажного кабинета:")
        print(all_info[2][3])
    elif command == "/schedule0":
        print("Полное расписание:")
        print(all_info[2])
    elif command == "/price":
        print("Стоимость занятий:")
        print(all_info[3])
    elif command == "/wish":
        print("Вы можете оставить обращение (пожелание, жалобу, благодарность).")
        wishes = input("Введите текст. Не забудте оставить телефон для обратной связи!: ")
        save()
    elif command == "/help":
        print("список команд:")
        print(all_info[4])
    else:
        print("Неопозанная команда. Просьба ознакомиться со списком команд через /help")
