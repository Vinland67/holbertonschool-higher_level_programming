#!/usr/bin/python3
"""Kvadratın ölçüsünü yoxlayan klass."""


class Square:
    """Kvadratı təmsil edən klass."""

    def __init__(self, size=0):
        """Kvadratı yeni ölçü ilə yaradır və yoxlayır.

        Args:
            size (int): Kvadratın tərəfinin ölçüsü (default 0).

        Raises:
            TypeError: Əgər size integer deyilsə.
            ValueError: Əgər size 0-dan kiçikdirsə.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
