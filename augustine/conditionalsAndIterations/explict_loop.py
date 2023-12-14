
people = ['Akira','Dianna','Syre','Augustine']
ages = ['20','23','25','27']
instruments =['Guitar','Bass','Piano','Violin']

for person,age,instrument  in zip(people,ages,instruments):
    print(person,age,instrument)