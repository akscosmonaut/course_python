"""Слайсы - объект, представляющий часть из целой последовательности
Указывается в []
[start:stop:step]
start - начальный индекс среза. Если не указан, используется 0.
stop -  Конечный индекс. Если не указан, используется 0.
step - Шаг выборки. Отрицательное значение позволяет строить срез из элементов в обратном порядке.
"""

#Примеры
#"отрезаем" от строки первые 10 символов (с 0-го по 11-ый, где 11-ый не включается в результирующую строку)
stroka = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry'
stroka[0:11]
>>> 'Lorem Ipsum'

#отрезаем от строки каждый второй символ в промежутке с 0-го по 11-ый элемент
stroka[0:11:2]
>>>'LrmIsm'

#"отрезаем" от строки в обратном порядке с 11-го символа по 0-й
stroka[11:0:-1]
>>> ' muspI mero'

#строка в перевёрнутом виде
stroka[::-1]
>>> 'yrtsudni gnittesepyt dna gnitnirp eht fo txet ymmud ylpmis si muspI meroL'