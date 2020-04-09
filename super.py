class Rectangle(object):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)


if __name__ == '__main__':
    print()
    square = Square(4)
    print(square.area())


class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length


if __name__ == '__main__':
    cube = Cube(4)
    print()
    print(cube.surface_area())
    print(cube.volume())


### A super() Deep Dive

class Square2(Rectangle):
    def __init__(self, length):
        super(Square2, self).__init__(length, length)


class Cube2(Square2):
    def surface_area(self):
        face_area = super(Square2, self).area()
        return face_area * 6

    def volume(self):
        face_area = super(Square2, self).area()
        return face_area * self.length


### HERANÇA MULTIPLA(MULTIPLE INHERITANCE)


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
        super().__init__()

    def area(self):
        return 0.5 * self.base * self.height


class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height
        super().__init__(self.base)

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area

    def area_2(self):
        base_area = super().area()
        triangle_area = super().area()
        return triangle_area * 4 + base_area


if __name__ == '__main__':
    pyramid = RightPyramid(base=2, slant_height= 4)
    print(RightPyramid.__mro__)  # method resolution order (or MRO) => informa como procurar metodos herdados
    print(pyramid.area())
    print(pyramid.area_2())
    print(pyramid.perimeter())