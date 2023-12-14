class Person:
    def __init__(self, age):
        self._age = age

    # getter
    @property
    def age(self):
        return f' Age is {self._age} '

    # setter
    @age.setter
    def age(self, age):
        if 18 <= age <= 99:
            self._age = age

        else:
            raise ValueError('Age must be within [18, 99')


person = Person(23)
print(person.age)
person.age = 45
print(person.age)
