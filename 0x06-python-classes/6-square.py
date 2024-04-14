#!/usr/bin/python3


class Square:
    """This represent a class Square."""

    def __init__(self, size=0):
        """This initializes the instance of a class Square.

        Args:
            size: side of the Square (1-side).
        """
        self.__size = size

    def area(self):
        """Calculate the area of a Square.

        returns the current square area.
        """
        self.__size ** 2

    @property
    def size(self):
        """Returns the size of a Square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """property setter for size.

        Args:
            value (int): size of a square (1-side).

        Raises:
            TypeError: Size must be an interger
            ValueError: Size must be greater then 0 (>0).
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Returns the current position of Square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ Property setter for POsition.

        Args:
            value turple:position of the Square.

        Raises:
            TypeError: position must be a tuple of 2 positive integers.
        """

        if not isinstance(value, turple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """prints in stdout the square with the character #
        """

        if self.__size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ",  end="")
                print("#" * (self.__size))
