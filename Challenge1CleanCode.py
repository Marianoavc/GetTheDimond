class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, origin, width, high):
        self.origin = origin
        self.width = width
        self.high = high

    def get_area(self):
        return self.width * self.high

    def print_coordenates(self):
        top_right = self.origin.x + self.width
        bottom_left = self.origin.y + self.high
        print('Starting Point (X)): ' + str(self.origin.x))
        print('Starting Point (Y)): ' + str(self.origin.y))
        print('End Point X-Axis (Top Right): ' + str(top_right))
        print('End Point Y-Axis (Bottom Left): ' + str(bottom_left))


def build_rectangle():
    point = Point(50, 100)
    rectangle = Rectangle(point, 90, 10)

    return rectangle


rectangle = build_rectangle()

print('Area: ' + str(rectangle.get_area()))
rectangle.print_coordenates()