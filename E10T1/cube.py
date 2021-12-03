from geometric_object import GeometricObject


class Cube(GeometricObject):
    def __init__(self, side_length: float, color: str, filled: bool):
        super().__init__(color, filled)
        self.__side_length = side_length

    def get_side_length(self):
        return self.__side_length

    def get_area(self):
        return 6 * self.__side_length ** 2

    def get_volume(self):
        return self.__side_length ** 3


if __name__ == "__main__":
    c = Cube(6, "black", True)
    print(c.get_volume())
