"""
Объявление функции
наличие входных и выходных параметров опционально
"""


# сама функция
def test_function():
    print(5)


# вызов функции
test_function()

"""
Объявление функции
- входные параметры описываются внутри скобок (типы данных указывать не обязательно)
- выходные параметры указываются после слова return
"""


def test_function1(value1: int, value2: str):
    print(value1)
    print(value2)
    return value1


# вызов функции
# если при вызове входные параметры будут не тех типов, которые описаны, то питон будет ругаться
test_function1(5, "10")

"""
Объявление функции с входными параметрами без типов
"""


def test_function2(value1, value2):
    print(value1)
    print(value2)
    return value1


# вызов функции со строгим соотношением параметра и значения (keyword arguments)
value_five = 5
value_ten = 10
test_function2(value1=value_five, value2=value_ten)

"""
Указание входных параметров через *args и **kwargs
args - arguments, kwargs - keyword arguments

При использовании *args все передаваемые значения упаковываются в кортеж, 
с которым внутри функции можно работать
"""


def test_function3(*values):
    print(type(values))  # values - это кортеж (tuple)
    print(values)  # values будет равен (3,8,10,18)
    print(values[3])  # 18


# вызов функции
test_function3(3, 8, 10, 18)

"""
При использовании **kwargs все передаваемые значения упаковываются в словарь, 
с которым внутри функции можно работать
"""


def test_function4(**kwvalues):
    print(type(kwvalues))  # kwalues - это словарь (dict)
    print(
        kwvalues)  # kwalues будет равен {"value1":3, "value2":8,
    # "value3":10, "value4":18}
    kwvalues["value1"] = 45  # меняем значение по ключу "value1"
    print(kwvalues["value1"])  # теперь "value1":45


# вызов функции
test_function4(value1=3, value2=8, value3=10, value4=18)