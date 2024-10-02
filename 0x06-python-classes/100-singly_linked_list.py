#!/usr/bin/python3
"""This is a module of a single linkedlist
"""


class Node:
    """This is a class representing a Nodeclear
    """
    def __init__(self, data, next_node=None) -> None:
        """This is a constructor

        Args:
            data (int): Data to be inserted
            next_node (Node, optional): _description_. Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """This is a getter method

        Returns:
            int: gets the data
        """
        return self._data

    @data.setter
    def data(self, value):
        """This is a setter method

        Args:
            value (int): sets the value

        Raises:
            TypeError: if the value is not an integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """Sets the nex_node field

        Returns:
            Node: the addres of the Node
        """
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """This is a setter method

        Args:
            value (Node or None): Sets the node

        Raises:
            TypeError: if the value is not Node or None
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    """This is singly linked list class
    """
    def __init__(self) -> None:
        """Constructor method
        """
        self.head = None

    def sorted_insert(self, value):
        """This method inserts a node in a sorted(ascending) manner

        Args:
            value (int): value to be inserted
        """
        new_node = Node(value)
        if not self.head or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node and value > current.next_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self) -> str:
        """This is to print the class

        Returns:
            str: prints the string in commandline
        """
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return '\n'.join(result)
