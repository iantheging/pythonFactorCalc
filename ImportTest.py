from classes import *

while True:
    print("\nRectangle Program: Please input points in a clockwise fashion in x,y form")
    p1x, p1y = input("Point 1: ").split(',')
    p2x, p2y = input("Point 2: ").split(',')
    p3x, p3y = input("Point 3: ").split(',')
    p4x, p4y = input("Point 4: ").split(',')
    p1 = Point(float(p1x), float(p1y))
    p2 = Point(float(p2x), float(p2y))
    p3 = Point(float(p3x), float(p3y))
    p4 = Point(float(p4x), float(p4y))
    r = Rectangle(p1, p2, p3, p4)
    userChoice = input("Enter p for perimeter of a for area: ")
    if userChoice is 'p':
        print(f'The perimeter is {r.perimeter()}')
    else:
        print(f"The area is {r.area()}")
    userEnd = input("Enter q to quit program: ")
    if userEnd is 'q':
        print("Goodbye")
        break
