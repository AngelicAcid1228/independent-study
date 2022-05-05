from LinkedList import LinkedList
from Node import Node

# Linked list testing
LL = LinkedList()
print("Is the list empty at the beginning: ", LL.is_empty())
LL.add_element_front(3)
LL.add_element_front(77)
LL.add_element_end(38)
LL.add_element_front(6)
print('Elements added into list: 6, 77, 3, 38')
print("Last element in the list:", LL.tail.data)
LL.remove_element_end()
print("Removed previous last element.Last element in the list is currently:", LL.tail.data)
print("Is the list empty after adding elements: ", LL.is_empty())
print("Is 3 in the list: ", LL.in_list(3))
print("What is the size of the list currently: ", LL.get_size())
LL.remove_element_end()
print("What is the size of the list currently after removing last element: ", LL.get_size())
print('What is the element at the front: ', LL.head.data)
print("Does 44 exist in the list: ", LL.in_list(44))
LL.add_element_front(42)
print('Adding 42 to the front of the list')
print("What is the first element: ", LL.head.data)

