# enumerate() > range(len(.....))

'''surnames = ['Rivest','Shamirah','Augustine']

for position , surname in enumerate(surnames,start=0) :
    print(position,surname)
'''

surnames = ['august','augustine','syre']
position = 0

while position < len(surnames):
    print(position, surnames[position])
    position +=1