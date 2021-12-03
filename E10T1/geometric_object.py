from abc import ABC, abstractmethod


class GeometricObject(ABC):
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_volume(self):
        pass

    def get_color(self):
        return self.color

    def set_color(self, color:str):
        self.color = color

    def get_filled(self):
        self.filled = True

    def set_filled(self, filled:bool):
        set.filled = filled

