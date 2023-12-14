from datetime import date, datetime


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def calculate_age(cls, name, birth_year):
        return cls(name, date.today().year - birth_year)

    def show(self):
        print(self.name + "'s age is: " + str(self.age))


augustine = Student('Augustine', 23)
augustine.show()

# create new object using the factory method
joy = Student.calculate_age("Joy", 2000)
joy.show()
