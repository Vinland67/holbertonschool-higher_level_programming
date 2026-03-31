#!/usr/bin/python3
"""Kvadratın sahəsini hesablayan klass."""


class Square:
    """Kvadratı təmsil edən klass."""

    def __init__(self, size=0):
        """Kvadratı yaradır və ölçünü yoxlayır.

        Args:
            size (int): Kvadratın tərəfinin ölçüsü (default 0).
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Kvadratın cari sahəsini qaytarır.

        Returns:
            Kvadratın sahəsi (size * size).
        """
        return self.__size * self.__size
