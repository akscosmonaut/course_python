from course_python.ls5_classes import Dog


class Body():
    def __init__(self):
        self.ears = 'long'
        self.legs = 'short'
        self.tale = 'big'

    def describe_body(self):
        print("Body with {} ears, {} legs, {} tale".format(self.ears, self.legs, self.tale))


class Spaniel(Dog):

    def __init__(self, name, age):
        super().__init__(name, age)
        # Выносим часть атрибутов в отдельный класс
        self.body = Body()

    def describe_spaniel(self):
        print("Spaniel has {} ears".format(self.ears))

    def roll_over(self):
        print("Spaniel {} rolled over!".format(self.name))