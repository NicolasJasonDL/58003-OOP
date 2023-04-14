from math import pi

class Circle():

    def __init__(self,r):
        self.radius = r

    def area(self):
        return pi*self.radius*self.radius

    def perimeter(self):
        return 2*pi*self.radius

r = float(input("Enter the radius of the circle: "))
SolvedCircle = Circle(r)
print("The area of the circle is:", SolvedCircle.area())
print("The perimeter of the circle is:", SolvedCircle.perimeter())