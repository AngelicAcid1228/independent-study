from Node import Node


class LinkedList:
    """The point of this class is to connect our single nodes containing data to a head pointer
    that points to a complete instance of a LinkedList"""

    def __init__(self):
        """ This constructor has a single head node """
        self.head = None
        self.tail = None
        self.size = 0

    def add_element_front(self, value):
        """ This method adds a new node to the front of the linked list by creating a new instance of Node
        and then adding in the value for it along with letting the head node be now the next node, and the new node
        becoming the head node """
        new_node = Node(value, self.head)
        self.head = new_node
        self.size += 1
        if self.size == 1:
            self.tail = self.head

    def add_element_end(self, value):
        """This method adds a new element to the end of the list. First a new node is initialized, then
        the tail element in the list give a next that is the new node. Finally the size of the list is updated
        and the new node is also specified as the end of the list."""
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def remove_element_front(self):
        """This element removes the first element from the list by replacing the next element in the list to be
        the head element in the list. This successfully removes the first original element"""
        self.head = self.head.next

    def remove_element_end(self):
        """This method runs through a while loop checking if the current element is not the tail, once it is
        then the loop breaks and that current value (which was the element before the tail) replaces the tail and
        removes the last element from the linked list"""
        current = self.head
        while current.next != self.tail:
            current = current.next
        self.tail = current

    def get_end(self):
        """This element returns the element at the end"""
        return self.tail

    def get_front(self) -> Node:
        """This method returns the element at the front"""
        return self.head

    def get_size(self) -> int:
        """This method returns the size of the linked list"""
        return self.size

    def is_empty(self) -> bool:
        """This method returns whether or not the list is empty """
        return self.size == 0

