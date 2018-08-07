import math

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def side_length(self):

        return l1 + l2 + l3

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

pA = Point(1, 1)
pB = Point(2, 2)
pC = Point(3, 1)
t = Triangle(pA, pB, pC)

print(t.side_length())
