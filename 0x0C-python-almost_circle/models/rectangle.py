#!/usr/bin/python3
"""
    contains class Rectangle which implements Base.
"""
from models.base import Base


class Rectangle(Base):
    """
        class Rectangle implements Base.
        Attributes:
            __width (int)
            __height (int)
            __x (int)
            __y (int)
        Methods:
            __init__()
            width()
            height()
            x()
            y()
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Initializes the class.
            Args:
                width (int): width of rectangle.
                height (int): height of rectangle.
                x (int)
                y (int)
                id (int): id of rectangle.
        """
        Base.__init__(self, id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
            getter function for __width
            Returns: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            setter function for width.
            Args:
                value (int): value to be set.
        """
        self.__width = value

    @property
    def height(self):
        """
            getter function for height
            Returns: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            setter function for height
            Args:
                value (int): value to be set.
        """
        self.__height = value

    @property
    def x(self):
        """
            getter function for x.
            Returns: x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
            setter function for x.
            Args:
                value (int): value to be set.
        """
        self.__x = value

    @property
    def y(self):
        """
            getter function for y
            Returns: y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
            setter function for y
            Args:
                value (int): value to be set.
        """
        self.__y = value