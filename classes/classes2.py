from numpy import shape


class Shape:
    def __init__(self):
        pass
    
    def area(self, length):
        self.length = area.length

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    
    def area(self):
        return self.length ** 2

#shape = Shape()
square = Square(int(input()))
print(shape.area())