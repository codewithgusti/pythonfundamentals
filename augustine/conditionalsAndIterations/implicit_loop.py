# multiple sequence using implicit

people = ['Akira','Dianna','Syre','Augustine']
ages = ['20','23','25','27']
instruments =['Guitar','Bass','Piano','Violin']

for data in zip(people,ages,instruments):
    person,age,instrument = data
    print(person,age,instrument)