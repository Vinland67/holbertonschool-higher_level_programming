#!/usr/bin/python3
"""Kvadratın ölçüsünü və koordinatlarını idarə edən klass."""


class Square:
    """Kvadratı təmsil edən klass."""

    def __init__(self, size=0, position=(0, 0)):
        """Kvadratı yaradır.

        Args:
            size (int): Kvadratın ölçüsü.
            position (tuple): Kvadratın koordinatları (x, y).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Size getter."""
        return self.__size

    @size.setter
    def size(self, value):
        """Size setter."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Position getter."""
        return self.__position

    @position.setter
    def position(self, value):
        """Position setter."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Sahəni hesablayır."""
        return self.__size * self.__size

    def my_print(self):
        """Kvadratı koordinatlara uyğun çap edir."""
        if self.__size == 0:
            print("")
            return

        # Y koordinatı üçün boş sətirlər (ancaq y > 0 olanda)
        if self.__position[1] > 0:
            for i in range(self.__position[1]):
                print("")

        # Kvadratın özünü çap edirik
        for i in range(self.__size):
            # X koordinatı üçün boşluqlar + '#' işarələri
            print(" " * self.__position[0] + "#" * self.__size)
