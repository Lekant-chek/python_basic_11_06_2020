"""
1 Реализовать функцию, принимающую два числа (позиционные аргументы)
 и выполняющую их деление. Числа запрашивать у пользователя,
 предусмотреть обработку ситуации деления на ноль.
"""
def divisor(num1, num2):
    """ Возвращает частное от деления"""
    return round(num1 / num2, 2)
while True:
    num1 = input('Введите число\n')
    num2 = input('Введите число отличное от нуля\n')
    if num1.isdigit() and num2.isdigit():
        num1 = int(num1)
        num2 = int(num2)
        if num2 == 0:
            num2 = input('Вы ввели нуль! Введите число\n')
            num2 = int(num2)
        break
    else:
        print('Ошибочный ввод. Введите числа\n')
print (divisor(num1, num2))