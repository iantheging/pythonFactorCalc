import math

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def perimeter(self):
        l1 = math.sqrt((self.p2.x - self.p1.x) ** 2 + (self.p2.y - self.p1.y) ** 2)
        l2 = math.sqrt((self.p3.x - self.p2.x) ** 2 + (self.p3.y - self.p2.y) ** 2)
        l3 = math.sqrt((self.p1.x - self.p3.x) ** 2 + (self.p1.y - self.p3.y) ** 2)
        return l1 + l2 + l3

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# controlled test
pA = Point(1, 1)
pB = Point(2, 2)
pC = Point(3, 1)
t = Triangle(pA, pB, pC)

print('{0:.4}'.format(t.perimeter()))

# user controlled test
print("\nPlease input the points in x,y format")
pax, pay = input("Point 1: ").split(',')
pa = Point(float(pax), float(pay))
pbx, pby = input("Point 2: ").split(',')
pb = Point(float(pbx), float(pby))
pcx, pcy = input("Point 3: ").split(',')
pc = Point(float(pcx), float(pcy))

t2 = Triangle(pa, pb, pc)

print('{0:.4}'.format(t2.perimeter()))
