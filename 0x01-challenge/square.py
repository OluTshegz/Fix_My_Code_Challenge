#!/usr/bin/python3
"""This module contains class Square"""


class Square():
    """This class represents a Square"""

    def __init__(self, width, height):
        """
        Is a class constuctor that initializes
        the width and height of the square
        Args:
            width (int): The width of the Square
            height (int): The height of the Square
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the width of the square"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height of the square"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area_of_my_square(self):
        """Returns the area of the square"""
        return self.__width * self.__height

    def permiter_of_my_square(self):
        """Returns the perimeter of the square"""
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Returns the string representation of the square"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
