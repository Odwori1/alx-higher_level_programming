#!/usr/bin/python3
"""class module goes here"""


class Node:
    """class Node that defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """this is the constructor

                              Args:
        data: data in the node
        next_node: next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """This getter func returns the data"""
        return self.__data

    @data.setter
    def data(self, value):
        """This setter func sets the data

         Raises:
          TypeError: if value is not an integer

        Args:
           value: value to set
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """This getter func returns the data
        Returns:
            the next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """This setter func sets the node

         Raises:
          TypeError: if node is not an objet

        Args:
           value: value to set
        """
        if value is not None and type(value) != Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """This is a class Square that defines a SinglyLinkedList"""

    def __init__(self):
        """this is the constructor"""
        self.head = None

    def __str__(self):
        """Method that print the entire list in stdout"""

        print_sll = ""
        current = self.head
        while current:
            print_sll += str(current.data) + "\n"
            current = current.next_node
        return print_sll[:-1]

    def sorted_insert(self, value):
        """Func that inserts a new Node into the correct sorted position
        Args:
            value: value to be inserted
        """
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        if value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return
        current = self.head
        while current.next_node and current.next_node.data < value:
            current = current.next_node
        if current.next_node:
            new_node.next_node = current.next_node
        current.next_node = new_node
