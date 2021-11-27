"""
Домашнее задание №1
Условный оператор: Возраст
* Попросить пользователя ввести возраст при помощи input и положить
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь:
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат
  работы функции в переменную
* Вывести содержимое переменной на экран
"""


def check_age():
    age = input('Введите свой возраст: ')
    try:
        age = int(age)
    except ValueError:
        print('Введено не число')

        if type(age) == int:
            if 0 < age <= 100:
                if age <= 6:
                    return 'Пользоватеь ходит в детский сад'
                elif 6 < age <= 17:
                    return 'Пользоватеь учится в школе'
                elif 17 < age <= 23:
                    return 'Пользоватеь учится в ВУЗе'
                elif 23 < age <= 65:
                    return'Пользоватеь работает'
                elif 65 < age <= 100:
                    return 'Пользователь пенсионер'
                else:
                    return 'Вы ввели некорректные данные'
            else:
                return 'Вы ввели некорректные данные'
        else:
            raise ValueError('Work with Positive Numbers Only')


age_variable =  check_age()


if __name__ == "__main__":
    print(age_variable)
