class Shapes():
    def shape(self):
        print("Shapes are")

class Triangle(Shapes):
    def shape(self):
        super().shape()
        print("Triangle")

class Rectangle(Triangle):
    def shape(self):
        super().shape()
        print("Rectangle")

class Circle(Rectangle):
    def circle(self):
        super().shape()
        print("circle")

x = Circle()
x.circle()