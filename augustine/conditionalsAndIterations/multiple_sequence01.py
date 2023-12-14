# Iterate over multiple sequences of the same length
# using range(len)

people = ['Akira','Dianna','Syre','Augustine']
ages = ['20','23','25','27']

for position in range(len(people)):
    person = people[position]
    age = ages[position]
    print(person,age)

