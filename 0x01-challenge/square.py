#!/usr/bin/python3

class square():
    
    width = 0
    height = 0

    
    def __init__(self, side_length):
        self.width = side_length
        self.height = side_length

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":

    s = square(side_length=12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
