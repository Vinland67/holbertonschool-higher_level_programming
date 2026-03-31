#!/usr/bin/python3
"""Düzbucaqlıları müqayisə edən (static method) klass."""


class Rectangle:
    """Düzbucaqlını təmsil edən klass."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Düzbucaqlını yaradır."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Width getter."""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Height getter."""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Sahəni hesablayır."""
        return self.__width * self.__height

    def perimeter(self):
        """Perimetri hesablayır."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Düzbucaqlını print_symbol ilə vizual təsvir edir."""
        if self.__width == 0 or self.__height == 0:
            return ""
        row = str(self.print_symbol) * self.__width
        rect_str = (row + "\n") * self.__height
        return rect_str[:-1]

    def __repr__(self):
        """Obyektin kod təsvirini qaytarır."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Obyekt silinərkən mesaj çap edir."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """İki düzbucaqlıdan sahəsi böyük olanı qaytarır.

        Args:
            rect_1 (Rectangle): Birinci düzbucaqlı.
            rect_2 (Rectangle): İkinci düzbucaqlı.

        Raises:
            TypeError: Əgər daxil edilənlər Rectangle obyekti deyilsə.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
