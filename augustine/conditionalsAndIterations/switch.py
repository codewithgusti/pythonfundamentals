# switch in python

day_input = input('Enter a day :')
day_number =int(day_input)

if 1<= day_number <=5:
    day = 'Weekday'
elif day_number == 6:
    day = 'Saturday'
    print(day)
elif day_number == 0:
    day = 'Sunday'
    
else:
    day = ''
    raise ValueError(str(day_number) + 'is not a valid day number')
