import math

class Figure:
    def __init__(self, __color=(255, 255, 255), *sides, filled=False):
        if not self._is_valid_sides(*sides):
            print("Invalid sides")
            return
        self.__sides = list(sides)
        self.__color = list(__color)
        self.filled = filled

    def get_sides_count(self):
        return len(self.__sides)

    def get_color(self):
        return self.__color

    def _is_valid_color(self, r, g, b):
        return all(isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b))

    def set_color(self, r, g, b):
        if self._is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def _is_valid_sides(self, *sides):
        return all(isinstance(side, int) and side > 0 for side in sides) and len(sides) == self.get_sides_count()

    def get_sides(self):
        return self.__sides.copy()

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self._is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    def __init__(self, color, radius, filled=False):
        super().__init__(color, radius, filled=filled)
        self.__radius = radius

    def get_sides_count(self):
        return 1

    def get_square(self):
        return math.pi * self.__radius ** 2

    def set_sides(self, radius):
        if self._is_valid_sides(radius):
            self.__radius = radius
            self.__sides = [radius]

    def _is_valid_sides(self, *sides):
        return all(isinstance(side, int) and side > 0 for side in sides) and len(sides) == 1


class Triangle(Figure):
    def __init__(self, color, side1, side2, side3, filled=False):
        super().__init__(color, side1, side2, side3, filled=filled)

    def get_sides_count(self):
        return 3

    def get_square(self):
        p = sum(self.get_sides()) / 2
        sides = self.get_sides()
        return math.sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]))


class Cube(Figure):
    def __init__(self, color, side_length, filled=False):
        super().__init__(color, *(side_length,) * 12, filled=filled)

    def get_sides_count(self):
        return 12

    def get_volume(self):
        side_length = self.get_sides()[0]
        return side_length ** 3

    def set_sides(self, side_length):
        if self._is_valid_sides(*(side_length,) * 12):
            self.__sides = list((side_length,) * 12)


# Тестовый код
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides([5, 3, 12, 4, 5]) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

