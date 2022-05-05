from LinkedList import LinkedList
from Node import Node

# Linked list testing
LL = LinkedList()
LL.add_element_front(3)
LL.add_element_front(66)
LL.add_element_front(6)
LL.remove_element_end()

print(LL.tail.data)
