# Class object and Namespace

class Person:
    species = 'Human'

print(Person.species)
Person.alive = True # added Dynamically
print(Person.alive)
man = Person() # inherited
print(man.species)
man.name = 'August'
man.surname = 'Shokane'
print(man.name,man.surname)