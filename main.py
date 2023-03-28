from course_python.ls5_classes import Dog
from course_python.ls6_inheritance import Spaniel

if __name__ == '__main__':
    my_dog = Dog("Henry", 7)

    # print(type(my_dog))
    # print(my_dog.name)
    # print(my_dog.age)
    # print(my_dog.word)

    # my_dog.sit("boy")
    # dog_word = my_dog.say()
    # print(dog_word)

    # print(my_dog.word)
    # my_dog.say()
    # print(my_dog.word)

    # Создание экземпляра дочернего класса
    his_dog = Spaniel("Bob", 3)

    # Вызов метода дочернего класса Spaniel
    his_dog.describe_spaniel()

    # Переопределение метода родительского класса
    my_dog.roll_over()
    his_dog.roll_over()


    his_dog.body.describe_body()

    print(type(his_dog.body))




