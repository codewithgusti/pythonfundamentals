# self argument

class Square:
    side = 8

    # self is a reference to an instance
    def area(self):
        return self.side ** 2


sq = Square()
print(sq.area())
sq.side = 10
print(sq.area())
