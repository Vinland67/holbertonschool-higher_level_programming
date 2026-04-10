#!/usr/bin/python3
"""
Abstrakt klaslar və Duck Typing-i nümayiş etdirən modul.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Bütün formalar üçün abstrakt baza klası."""

    @abstractmethod
    def area(self):
        """Sahəni hesablayan abstrakt metod."""
        pass

    @abstractmethod
    def perimeter(self):
        """Perimetri hesablayan abstrakt metod."""
        pass


class Circle(Shape):
    """Dairə klası."""

    def __init__(self, radius):
        """Radiusu mənimsədir."""
        self.radius = radius

    def area(self):
        """Dairənin sahəsini hesablayır."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Dairənin perimetrini hesablayır."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Düzbucaqlı klası."""

    def __init__(self, width, height):
        """Eni və hündürlüyü mənimsədir."""
        self.width = width
        self.height = height

    def area(self):
        """Düzbucaqlının sahəsini hesablayır."""
        return self.width * self.height

    def perimeter(self):
        """Düzbucaqlının perimetrini hesablayır."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Duck typing vasitəsilə formanın məlumatlarını çap edir."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
