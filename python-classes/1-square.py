#!/usr/bin/python3
"""Kvadratın ölçüsü ilə birlikdə təyin olunduğu klass."""


class Square:
    """Kvadratı təmsil edən klass."""

    def __init__(self, size):
        """Kvadratı yeni ölçü ilə yaradır.

        Args:
            size: Kvadratın tərəfinin ölçüsü.
        """
        self.__size = size
