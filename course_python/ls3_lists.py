def list_with_comprehensions():
    list1 = [5, 15, 16, 23, 19, 23, -98, 43, -13, -9]
    # создаём новый список из элементов первого списка, выбрав из него все отрицательные числа
    # выражение пройдётся циклом по первому списку и каждый элемент проверит на отрицательность
    list2 = [i for i in list1 if i < 0]
