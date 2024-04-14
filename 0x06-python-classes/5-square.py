#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Thia represent a Square Class."""


    def __init__(self, size=0):
        """initializing the class
        
        args:size int represent the size of the square 

        """

        self.__size = size

    def area(self):
        """ Calulate the area of Square.

            return: the current  of a square
        """

        return self.__size **2

    @property

    def size(self):
        """ Returns the size of a square."""
        return self.__size

    @size.setter

    def size(self, value):
        """Property setter for size.

        args:
            value int: size of a square (1-side)

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0

            """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):

        if self.size == 0:
            print()
        for i in range(self.__size):
            print("#" * (self.__size))


