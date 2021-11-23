from abc import ABC, abstractmethod


class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        return f"{self.name}: {self.age}, {self.height}"


class Serializer(ABC):

    def serialize(self, person):
        name = self.format_name(person.name)
        age = self.format_age(person.age)
        height = self.format_height(person.height)
        return self.line_template() % (name, age, height)

    @abstractmethod
    def format_name(self, name):
        pass

    @abstractmethod
    def format_age(self, age):
        pass

    @abstractmethod
    def format_height(self, height):
        pass

    @abstractmethod
    def line_template(self):
        pass


class NaturalSerializer(Serializer):
    def format_name(self, name):
        return name

    def format_age(self, age):
        return f"{age} years old"

    def format_height(self, height):
        return f"{height}cm tall"

    def line_template(self):
        return "%s is %s and %s"


p = Person("Ann", 31, 168)
print(p)

s = NaturalSerializer()
print(s.serialize(p))