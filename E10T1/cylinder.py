from geometric_object import GeometricObject


class Cylinder(GeometricObject):
    def __init__(self, radius:float, height:float, color:str, filled:bool):
        super().__init__(color, filled)
        self.__PI = 3.14
        self.__radius = radius
        self.__height = height

    def get_radius(self):
        return self.__radius

    def get_height(self):
        return self.__height

    def get_area(self):
        return self.__PI * self.__radius**2 + 2 * self.__PI * self.__radius * self.__height

    def get_volume(self):
        return self.__PI * self.__radius**2 * self.__height


if __name__ == "__main__":
    c = Cylinder(3, 4, "pink", False)
    print(c.get_area())