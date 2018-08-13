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


class Rectangle:
    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        if self.check_rect() is not True:
            print("This is not a rectangle")

    def side_lengths(self):
        l1 = math.sqrt((self.p2.x - self.p1.x) ** 2 + (self.p2.y - self.p1.y) ** 2)
        l2 = math.sqrt((self.p3.x - self.p2.x) ** 2 + (self.p3.y - self.p2.y) ** 2)
        l3 = math.sqrt((self.p4.x - self.p3.x) ** 2 + (self.p4.y - self.p3.y) ** 2)
        l4 = math.sqrt((self.p1.x - self.p4.x) ** 2 + (self.p1.y - self.p4.y) ** 2)
        return l1, l2, l3, l4

    def perimeter(self):
        s1, s2, s3, s4 = self.side_lengths()
        return s1 + s2 + s3 + s4

    def area(self):
        s1, s2, s3, s4 = self.side_lengths()
        return s1 * s2

    def check_rect(self):
        s1, s2, s3, s4 = self.side_lengths()
        if s1 != s3 and s2 != s4:
            return False
        return True

    def check_square(self):
        s1, s2, s3, s4 = self.side_lengths()
        if s1 == s2 and s2 == s3 and s3 == s4:
            return True
        return False


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
