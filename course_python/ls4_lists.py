#генерация списка из цифр от 0 до 9
list2 = [i for i in range(0, 9)]
>>>  [0, 1, 2, 3, 4, 5, 6, 7, 8]

#генерация списка из чётных чисел от 0 до 20
list3 = [i for i in range(0, 20, 2)]
>>> [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

#сохранение содержимого списка в переменные и новый список
list3 = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
a, *b, c = list3
"""
a будет равно 0,
*b будет равно [2, 4, 6, 8, 10, 12, 14, 16]
c будет равно 18

"""

#поменять значение двух переменных местами
x = 5
y = 10
x, y = y, x

#создание списка через *
c = [0] * 3
>>> [0, 0, 0]

#создание списка из подсписков через *
d = [c] * 3
>>> [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
