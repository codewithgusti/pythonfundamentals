# bike class

class Bike:
    def __init__(self,color,frame_material):
        
        self.color=color
        self.frame_material=frame_material
        
    # methods of the bike
    def brake(self):
        print('Braking')
        
# create the instance of the class bike

red_bike = Bike('Red','Carbon fiber')
blue_bike = Bike('Blue','Steel')  

# let's inspect the object we have, the instance of the class
# red bike
print(red_bike.color)
print(red_bike.frame_material)

# blue bike
print(blue_bike.color)
print(blue_bike.frame_material)

# the action
red_bike.brake()