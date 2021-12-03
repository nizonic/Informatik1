from geometric_object import GeometricObject


class Cone(GeometricObject):
    def __init__(self, radius:float, vertical_height:float, lant_height:float, color:str, filled:bool):
        super().__init__(color, filled)
        self.__PI = 3.14
        self.__radius = radius
        self.__vertical_height = vertical_height
        self.__slant_height = lant_height

    def get_radius(self):
        return self.__radius

    def get_vertical_height(self):
        return self.__vertical_height

    def get_slant_height(self):
        return self.__slant_height

    def get_area(self):
        return round(self.__PI * self.__radius**2 + self.__PI * self.__radius * self.__slant_height, 2)

    def get_volume(self):
        return round(1/3 * self.__PI * self.__radius**2 * self.__vertical_height, 2)


if __name__ == "__main__":
    c = Cone(2,5,3, "yellow", True)
    print(c.get_color())