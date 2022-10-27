#сложение нескольких строк
stroka1 = "Lorem Ipsum is simply dummy text of the printing and typesetting " \
         "industry"
stroka2 = 'Lorem Ipsum is simply dummy text of the printing and typesetting ' \
          'industry'
stroka3 = stroka1 + stroka2
stroka4 = stroka1 + ' ' + stroka2
stroka5 = stroka1 + ' ' + stroka2

#способы вставки строк для распечатки через +
x = 5
print("Х равен: " + str(x))
>>> "X равен: 5"

#способы вставки строк для распечатки через format()
result = "Х равен: {} , а Y равен:7".format(x)
print(result)
>>> "Х равен: 5 , а Y равен:7"

#переменных в format() может быть несколько
result = "Наш Х равен: {} {} {} {} {}, а y равен:7".format(x, 5, 6, 7, 8)
print(result)
>>> "Наш Х равен: 5 5 6 7 8, а y равен:7"

#можно задавать порядок упоминания переменных в строке с помощью цифр
result = "Наш Х равен: {0} {1} {2} {3} {4}, а y равен:7".format(x, 5, 6, 7, 8)
print(result)
>>> "Наш Х равен: 5 5 6 7 8, а y равен:7"

#также можно указывать переменные для вставки в строку явно
result = "Наш Х равен: {digit1} {digit2}, а y равен:7".format(digit1=4,
                                                              digit2=x)
print(result)
"Наш Х равен: 4 5, а y равен:7"

#способы вставки строк для распечатки через f-string
result2 = f'Значение х равно:{x}'
print(result2)

#способы вставки строк для распечатки через %
#%s - если указано s, то значит, в это место вставится значение типа string
print('Значение х равно: %s' % x)
>>> "Значение х равно: 5"


#функции для работы со строками

#делает первую букву строки заглавным
sss = 'moscow'
sss.capitalize()
>>> 'Moscow'

#делает первую букву строки строчным
sss1 = 'Tokyo'
ss1.lower()
>>> 'tokyo'


#разделение строки на список строк по указанному символу
stroka = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry'
# по дефолту split() делит строку по пробелу
stroka.split()
>>> ['Lorem', 'Ipsum', 'is', 'simply', 'dummy', 'text', 'of', 'the', 'printing',
 'and', 'typesetting', 'industry']
#деление строки на список символов по символу "у"
stroka.split('y')
>>> ['Lorem Ipsum is simpl', ' dumm', ' text of the printing and t',
 'pesetting industr', '']

#альтернативный способ разделения строки на список строк с помощью list comprehensions
stroka = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry'
list1 = [i for i in stroka]
print(list1)
>>> ['L', 'o', 'r', 'e', 'm', ' ', 'I', 'p', 's', 'u', 'm', ' ', 'i', 's', ' ',
 's', 'i', 'm', 'p', 'l', 'y', ' ', 'd', 'u', 'm', 'm', 'y', ' ', 't', 'e',
 'x', 't', ' ', 'o', 'f', ' ', 't', 'h', 'e', ' ', 'p', 'r', 'i', 'n', 't',
 'i', 'n', 'g', ' ', 'a', 'n', 'd', ' ', 't', 'y', 'p', 'e', 's', 'e', 't',
 't', 'i', 'n', 'g', ' ', 'i', 'n', 'd', 'u', 's', 't', 'r', 'y']
