"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def sum_max_2(a, b, c):
    res = sum([a, b, c]) - min(a, b, c)
    return res
print(sum_max_2(10, 3, 1))