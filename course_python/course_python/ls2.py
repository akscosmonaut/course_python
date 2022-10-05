def test_function(value1: int, value2: str):
    print(value1)
    print(value2)
    return value1

# *args и **kwargs
# args - arguments
#    (value1, value2)
# kwargs - keyword arguments
# (value1=5, value2=10)


def test_function2(*values):
    print(type(values))
    print(values)
    print(values[3])


def test_function3(**kwvalues):
    print(type(kwvalues))
    kwvalues["value1"] = 45
    print(kwvalues)