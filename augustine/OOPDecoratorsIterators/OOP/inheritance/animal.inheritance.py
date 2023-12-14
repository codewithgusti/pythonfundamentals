
# superclass

class Animal:
    name = ''

    def eat(self):
        print('i can eat')

# subclass
# inherit from animal
class Dog(Animal):

    def display(self):
        print('My name is', self.name)
        
dog = Dog()
dog.name= 'syre'
dog.eat()
dog.display()