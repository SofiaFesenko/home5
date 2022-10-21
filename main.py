class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y or self.z != other.z

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y and self.z < other.z

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y and self.z > other.z

    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y and self.z <= other.z

    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y and self.z >= other.z


print(Point(0, 0, 0) == Point(0, 0, 0))
print(Point(0, 0, 0) != Point(0, 1, 0))
print(Point(0, 43, 0) < Point(0, 0, 0))
print(Point(1, 0, 0) > Point(0, 0, 0))
print(Point(-8, -110, -9) <= Point(0, 0, 19))
print(Point(0, 0, 0) >= Point(0, 0, 0))


class Vegetables:
    def __init__(self, vegetables):
        self._vegetables = vegetables

    @property
    def vegetables(self):
        return self._vegetables

    @vegetables.setter
    def vegetables(self, new_vegetables):
        self._vegetables = new_vegetables
        print(self._vegetables)

    @vegetables.deleter
    def vegetables(self):
        print('delete')
        del self._vegetables


veg = Vegetables('potato')
print(veg.vegetables)

veg.vegetables = 'tomato'
print(veg.vegetables)

del veg.vegetables
print(veg.vegetables) #буде помилка


class Calculate:
    def __init__(self, one):
        self.one = one

    def __add__(self, other):
        return self.one + other.one

    def __sub__(self, other):
        return self.one - other.one

    def __mul__(self, other):
        return self.one * other.one

    def __divmod__(self, other):
        if other.one == 0:
            print('you can`t')
        else:
            return self.one / other.one

    def __pow__(self, other):
        return self.one ** other.one


c1 = Calculate(7)
c2 = Calculate(0)

c3 = c1 + c2
print(c3)

c3 = c1 - c2
print(c3)

c3 = c1 * c2
print(c3)

print(divmod(c1, c2))

c3 = c1 ** c2
print(c3)
