from math import pi

class Bubble:
    def __init__(self, capacity=1):
        self.capacity = capacity
        if type(capacity).__name__ not in ("int", "float"):
            raise ValueError("int or float capacity value is expected")

    #defining functions for sphere radius and square counting
    #depending on sphere capacity
    
    @property
    def radius(self):
        radius = ((3*self.capacity)/(4*pi))**(1/3)
        return radius

    @property
    def square(self):
        square = 4*pi*(self.radius**2)
        return square

    #setting the rules for addition and subtraction of
    #two spheres and returning new sphere object as a result

    def __add__(self, other):
        return Bubble(self.capacity + other.capacity)

    def __sub__(self, other):
        return Bubble(self.capacity - other.capacity)

a = Bubble(5)
b = Bubble(3)

print(a.capacity, b.capacity)
print(a.radius, b.radius)
print(a.square, b.square)

c = a+b

print(a.capacity, b.capacity)
print(a.radius, b.radius)
print(a.square, b.square)

print(c.capacity)
print(c.radius)
print(c.square)
