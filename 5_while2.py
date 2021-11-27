"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую

"""

questions_and_answers = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую", "Что будешь делать?": "Сидеть дома", "А ты кто?": "Сущность в виде гномика", "Чё?": "Ниче" }


def ask_user(questions_and_answers):
    while True:
        user_ask = input('Вводи вопрос уже: ')
        for key, value in questions_and_answers.items():
            if user_ask == key:
                print(value)
            else:
                pass


if __name__ == "__main__":
    ask_user(questions_and_answers)
