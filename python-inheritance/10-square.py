#!/usr/bin/python3
"""
Module for Square class that inherits from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a square using Rectangle."""

    def __init__(self, size):
        """
        Initialize the square with size.

        Args:
            size (int): The size of the square's side.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
