#  Create a class (2-D vector) and use it to create another class representing a 3-D
# vector

class TwoVector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(f"The vector is {self.x}i + {self.y}j")


class ThreeVector(TwoVector):
    def __init__(self, x , y,z):
        
     super().__init__( x , y)
     self.z = z
    def show(self):
        print(f"The vector is {self.x}i + {self.y}j + {self.z}k")


a = TwoVector(2,3)
a.show()
b = ThreeVector(6,8,5)
b.show()