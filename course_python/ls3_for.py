def loop_with_break():
    number = 0
    for number in range(10):
    # for number in range(10) - это означает, что number будет
    # принимать значения [0,1,2,3,4,5,6,7,8,9] и цикл будет проходить 10 раз
        if number == 5:
            break  # когда выполнится этот if, то цикл прервётся
                   # и всё, что ниже break не будет выполняться)
        print('Значение number: ' + str(number))
    print('Выход из цикла')


def loop_with_continue():
    number = 0
    for number in range(10):
        if number == 5:
            continue  # когда выполнится этот if, то текущая итерация прервётся,
                      # цикл перейдёт на другую итерацию, код после contunue выполняться не будет
            print('if')
        print('Значение number: ' + str(number))
    print('Выход из цикла')


def loop_with_pass():
    number = 0
    for number in range(10):
        if number == 5:
            pass  # ни итерация, ни цикл прерываться не будут
                  # pass никак не влияет на работу цикла, используется как заглушка
            print('if')
        print('Значение number: ' + str(number))
    print('Выход из цикла')
