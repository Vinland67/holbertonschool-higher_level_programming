#!/usr/bin/python3
"""Kvadratın ölçüsünü idarə edən (getter/setter) klass."""


class Square:
    """Kvadratı təmsil edən klass."""

    def __init__(self, size=0):
        """Kvadratı yaradır.

        Args:
            size (int): Kvadratın tərəfinin ölçüsü (default 0).
        """
        self.size = size

    @property
    def size(self):
        """Ölçünü geri qaytarır (Getter)."""
        return self.__size

    @size.setter
    def size(self, value):
        """Ölçünü təyin edir və yoxlayır (Setter)."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Kvadratın sahəsini qaytarır."""
        return self.__size * self.__size
