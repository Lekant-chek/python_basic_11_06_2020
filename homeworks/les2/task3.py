"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""
while True:
    month = input('Введите число от 1 до 12\n')
    if month.isdigit():
        break
    else:
        print('Ошибочный ввод. Введите число\n')
dict
seasons = {
    '(12, 1, 2)': 'зима', '(3, 4, 5)':'весна', '(6, 7, 8)':'лето', '(9, 10, 11)':'осень'
}

seas_keys = list(seasons.keys())
for item in seas_keys:
    if str(month) in item:
        print(seasons[item])