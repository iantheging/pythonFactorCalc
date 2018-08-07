x = 2
y = 3
print(x, y) # initial values

def change_values(a, b):
    global x
    x = a * 2
    global y
    y = b * 2

change_values(x, y)
print(x, y)
