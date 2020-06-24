"""1/ Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
"""
name = 'Фантом'
age = 100
genom = 'AUCCTAATTUA'
print('Данные о фаге:')
print(f'Про него известно: геном - {genom}, имя - {name}, возраст - {age}')
user_name = input('Введите имя\n')
while True:
    user_age = input('Введите возраст\n')
    if user_age.isdigit():
        user_age = int(user_age)
        break
    print('Возраст должен быть числом')
user_target = input('Что Вы планируете делать 1 июля? ')
print(f'Вас зовут {user_name}, Вам {user_age} лет. Ваши планы на 1 июля: {user_target}.')