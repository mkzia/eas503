import math
class Circle:

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius**2


    def __repr__(self):
        return "Circle with radius " + str(self.radius)
    def __str__(self):
        return "Circle with radius " + str(self.radius)

c1 = Circle(10)
c2 = Circle(5)

# print(c1)
# print(c2)
# print(c2.get_area())


# lets does c1 + c2 have any meaning? no
# https://thepythonguru.com/python-operator-overloading/

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius**2

    def __str__(self):
        return "Circle with radius " + str(self.radius)

    def __add__(self, another_circle):
        return Circle(self.radius + another_circle.radius)


c1 = Circle(10)
c2 = Circle(5)
c3 = c1 + c2
print(c3)


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius**2

    def __str__(self):
        return "Circle with radius " + str(self.radius)

    def __add__(self, another_circle):
        return Circle(self.radius + another_circle.radius)

    def __gt__(self, another_circle):
        return self.radius > another_circle.radius

    def __lt__(self, another_circle):
        return self.radius < another_circle.radius



c1 = Circle(10)
c2 = Circle(5)
print(c1 < c2)



class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, another_point):
        return Point(self.x + another_point.x, self.y + another_point.y)

    def __sub__(self, another_point):
        return Point(self.x - another_point.x, self.y - another_point.y)

    def __str__(self):
        return f'{self.x}, {self.y}'

p1 = Point(3, 4)
p2 = Point(8, 6)
print(p2+p1)

import math
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, another_point):
        return Point(self.x + another_point.x, self.y + another_point.y)

    def __sub__(self, another_point):
        return Point(self.x - another_point.x, self.y - another_point.y)

    def length(self):
        return math.sqrt(self.x**2 + self.y**2)

    def distance(self, another_point):
        return (self - another_point).length()

    def __str__(self):
        return f'{self.x}, {self.y}'

p1 = Point(3, 4)
p2 = Point(8, 6)
print(p1.distance(p2))


###

class MyRange:

    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.value = 0
        return self

    def __next__(self):
        if self.value < self.limit:
            output = self.value
            self.value += 1
            return output
        else:
            raise StopIteration


i = iter(MyRange(10))
next(i)
for ele in MyRange(10):
    print(ele)


class PowX:
    def __init__(self, limit, power):
        self.limit = limit
        self.power = power

    def __iter__(self):
        self.value = 0
        return self

    def __next__(self):
        if self.value < self.limit:
            output = self.value**self.power
            self.value += 1
            return output
        else:
            raise StopIteration


for ele in PowX(10, 3):
    print(ele)


## lets use generator

def PowX(limit, power):
    value = 0
    while value < limit:
        yield value**power
        value += 1

for ele in PowX(10, 3):
    print(ele)

new_list = []
for number in numbers:

    if number % 2 == 0
        new_list.append(number)
        I am here!!
