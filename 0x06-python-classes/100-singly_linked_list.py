#!/usr/bin/python3
class Node:
    """
    This is a class for define a node for linked list

    Attributes:
       attr1 (data): data of the node
       attr2 (next_node): object to the next node
    """
    def __init__(self, data, next_node=None):
        """
        The constructor of the class Node

        Args:
           param1 (data): data of the node
           param2 (next_node): object to the next node
        """
        if type(data) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = data

        if next_node is not None and type(next_node) != Node:
            raise TypeError("next_node must be a Node Object")
        self.__next_node = next_node

    @property
    def data(self):
        """
        getter and setter of data
        """
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        getter and setter of next_node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and type(value) != Node:
            raise TypeError("next_node must be a Node Object")
        self.__next_node = value


class SinglyLinkedList:
    """
    This is a class for define a Linked list

    Attributes:
       attr1 (head): Head of the linked list
    """
    def __init__(self):
        """
        This is the constructur of the class SinglyLinkedList

        Args:
           param1 (head): Head of the linked list
        """
        self.head = None

    def __str__(self):
        """
        This is a function str
        """
        temp = self.head
        str1 = ""
        while temp is not None:
            str1 += str(temp.data)
            str1 += "\n"
            temp = temp.next_node

        str1 = str1[:len(str1) - 1]

        return str1

    def sorted_insert(self, value):
        """
        This is a function for create and add sorted nodes

        Args:
           param1 (value): Value of the new node
        """
        if self.head is None:
            self.head = Node(data=value)
            return

        temp = self.head

        if temp.data > value:
            new = Node(data=value, next_node=temp)
            self.head = new
            return

        while temp.next_node is not None:
            if temp.next_node.data > value:
                new = Node(data=value, next_node=temp.next_node)
                temp.next_node = new
                return
            temp = temp.next_node

        temp.next_node = Node(data=value)
