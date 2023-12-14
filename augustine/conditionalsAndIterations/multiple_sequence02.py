# using enumerate function

people = ['Akira','Dianna','Syre','Augustine']
ages = ['20','23','25','27']

for position , person in enumerate(people):
    age = ages[position]
    print(person,age)