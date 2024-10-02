#!/usr/bin/python3
"""This module defines the class Square"""


class Square:
    """This is the definition of Square class

    Attributes:
        __size(int): Size of the square
        __position(tuple): Private instance representing tuple

    Methods:
        area(self): returns the area of of square
        size(self): getter method
        size(self, value): setter method
        my_print(self):print # int the stdout

    """
    def __init__(self, size=0, position=(0, 0)):
        """This method initializes the size variable

        Args:
            size(int):size of the square
            position(tuple): the position of the square

        Raises:
            TypeError:if the size is not integer
            ValueError: if size is less than 0

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.size = size
        self.position = position

    @property
    def size(self):
        """This is a getter method

        Returns:
            int: value of size

        """
        return self.__size

    @size.setter
    def size(self, value):
        """This is a setter method

        Args:
            value: value to set to size

        Raises:
            TypeError: if the size is not an integer
            ValueError: if the size is < 0

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """This is a public instance method

        Returns:
            int:value of the area

        """
        return self.__size * self.__size

    @property
    def position(self):
        """Getter method to retrieve pos

        Returns:
            tuple: Position of the square

        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method to set positin

        Args:
            value (tuple): new position for square

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
            ValueError: If position values are not positive integers.

        """
        if not isinstance(value, tuple) or len(value) != 2\
        or not all(isinstance(v, int) and v >= 0 for v in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def my_print(self):
        """This is a public instance method

        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
                for _ in range(self.__size):
                    print(" " * self.__position[0] + "#" * self.__size)
