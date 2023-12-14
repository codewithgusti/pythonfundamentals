class Room:
    def __init__(self, breadth, length):
        self.breadth = breadth
        self.length = length

    def calculate_area(self):
        return self.length * self.breadth


room1 = Room(42.5, 30.8,)
print(f'the area of the room is : {room1.calculate_area()}')
